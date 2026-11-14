#!/usr/bin/env python3
"""Evaluate the handbook chatbot on a set of test questions (Task 2).

For every question and every model it records the answer, the retrieved
sources and latency, plus two automatic signals:

- retrieval_hit: at least one retrieved chunk comes from an expected page
- keyword_score: fraction of expected keyword groups found in the answer

A question may list earlier user turns under "history"; they are asked first (with the
model's real answers kept as chat history) to test follow-up questions.

Automatic scores are only a guide. The output CSV has an empty `label` column
to fill in by hand (correct / incorrect / incomplete / ambiguous) for the report.

Usage:
    python evaluate.py
    python evaluate.py --models qwen2.5:0.5b qwen2.5:1.5b qwen2.5:3b
    python evaluate.py --questions eval/cs_handbook_questions.json --limit 5
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import time
from datetime import datetime
from pathlib import Path
from typing import List, Sequence, Union

from rag import RAGPipeline, get_settings
from rag.config import SOURCE_ROOT

REFUSAL_PATTERNS = ("could not find", "not mentioned", "does not contain", "no information", "not provided", "don't know", "do not know")

KeywordGroup = Union[str, Sequence[str]]


def _normalise(text: str) -> str:
    return re.sub(r"\s+", "", text.lower())


def keyword_score(answer: str, keywords: Sequence[KeywordGroup]) -> float:
    """Each group is a string or a list of alternatives; a group matches if any alternative appears."""
    if not keywords:
        return float("nan")
    answer_n = _normalise(answer)
    hits = 0
    for group in keywords:
        alternatives = [group] if isinstance(group, str) else list(group)
        hits += any(_normalise(alt) in answer_n for alt in alternatives)
    return hits / len(keywords)


def is_refusal(answer: str) -> bool:
    lowered = answer.lower()
    return any(pattern in lowered for pattern in REFUSAL_PATTERNS)


def ask_with_retry(pipeline: RAGPipeline, question: str, history: list, attempts: int = 3):
    """A remote Ollama server can drop a connection now and then; don't lose a long run to it."""
    for attempt in range(1, attempts + 1):
        try:
            return pipeline.ask(question, history)
        except Exception as exc:
            if attempt == attempts:
                raise
            wait = 10 * attempt
            print(f"  ! {type(exc).__name__}: {exc} - retrying in {wait}s", flush=True)
            time.sleep(wait)


def error_row(model: str, item: dict, exc: Exception) -> dict:
    return {
        "model": model, "id": item["id"], "category": item["category"], "question": item["question"],
        "history": " / ".join(item.get("history", [])), "reference": item.get("reference", ""),
        "answer": "", "retrieved": "", "retrieval_hit": "", "keyword_score": "", "refused": False,
        "latency_s": 0.0, "error": f"{type(exc).__name__}: {exc}", "label": "", "notes": "",
    }


def evaluate_model(model: str, questions: List[dict], args) -> List[dict]:
    settings = get_settings(llm_model=model, top_k=args.top_k, data_dir=args.data_dir)
    pipeline = RAGPipeline(settings)
    pipeline.ensure_index()
    rows = []
    for item in questions:
        try:
            history = []
            for previous in item.get("history", []):
                reply = ask_with_retry(pipeline, previous, history)
                history += [{"role": "user", "content": previous}, {"role": "assistant", "content": reply.answer}]
            response = ask_with_retry(pipeline, item["question"], history)
        except Exception as exc:  # keep going; the row records the failure
            rows.append(error_row(model, item, exc))
            print(f"[{model}] {item['id']} ERROR {exc}", flush=True)
            continue
        retrieved_pages = sorted({c.page for c in response.sources if c.page})
        expected_pages = set(item.get("pages", []))
        answerable = item.get("answerable", True)
        row = {
            "model": model,
            "id": item["id"],
            "category": item["category"],
            "question": item["question"],
            "history": " / ".join(item.get("history", [])),
            "reference": item.get("reference", ""),
            "answer": response.answer,
            "retrieved": "; ".join(f"{c.label} ({c.score:.2f})" for c in response.sources),
            "retrieval_hit": (bool(expected_pages & set(retrieved_pages)) if expected_pages else ""),
            "keyword_score": round(keyword_score(response.answer, item.get("keywords", [])), 2)
            if answerable
            else "",
            "refused": is_refusal(response.answer),
            "latency_s": response.latency_s,
            "error": "",
            "label": "",  # fill in manually: correct / incorrect / incomplete / ambiguous
            "notes": "",
        }
        rows.append(row)
        print(f"[{model}] {item['id']} kw={row['keyword_score']} hit={row['retrieval_hit']} {response.latency_s:.1f}s", flush=True)
    return rows


def summarise(rows: List[dict]) -> str:
    lines = [
        "| Model | Questions | Retrieval hit rate | Mean keyword score | Out-of-scope refusals | Answerable but refused | Mean latency (s) |",
        "|---|---|---|---|---|---|---|",
    ]
    errors = sum(bool(r["error"]) for r in rows)
    for model in dict.fromkeys(r["model"] for r in rows):
        subset = [r for r in rows if r["model"] == model and not r["error"]]
        hits = [r["retrieval_hit"] for r in subset if r["retrieval_hit"] != ""]
        scores = [r["keyword_score"] for r in subset if r["keyword_score"] != "" and r["keyword_score"] == r["keyword_score"]]
        oos = [r for r in subset if r["keyword_score"] == ""]
        answerable = [r for r in subset if r["keyword_score"] != ""]
        lines.append(
            f"| {model} | {len(subset)} | {sum(hits) / max(len(hits), 1):.0%} | "
            f"{statistics.mean(scores) if scores else 0:.2f} | "
            f"{sum(r['refused'] for r in oos)}/{len(oos)} | "
            f"{sum(r['refused'] for r in answerable)}/{len(answerable)} | "
            f"{statistics.mean(r['latency_s'] for r in subset) if subset else 0:.1f} |"
        )
    if errors:
        lines += ["", f"{errors} question(s) failed after retries and are excluded above (see the `error` column)."]
    return "\n".join(lines)


def write_report(rows: List[dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "results.csv", "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / "results.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    md = ["# Evaluation results", "", f"Generated {datetime.now():%Y-%m-%d %H:%M}", "", "## Summary", "", summarise(rows), ""]
    md += ["## Answers", ""]
    for r in rows:
        md += [
            f"### {r['id']} · {r['model']} · {r['category']}",
            *([f"*Asked after:* {r['history']}", ""] if r["history"] else []),
            f"**Q:** {r['question']}",
            "",
            f"**Reference:** {r['reference']}",
            "",
            f"**Answer:** {r['answer']}" if not r["error"] else f"**Error:** {r['error']}",
            "",
            f"*Retrieved:* {r['retrieved'] or '(none)'}  ",
            f"*Retrieval hit:* {r['retrieval_hit']} · *keyword score:* {r['keyword_score']} · *latency:* {r['latency_s']}s",
            "",
        ]
    (out_dir / "summary.md").write_text("\n".join(md), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the RAG chatbot on test questions")
    parser.add_argument("--questions", default=str(SOURCE_ROOT / "eval" / "cs_handbook_questions.json"))
    parser.add_argument("--models", nargs="+", default=[get_settings().llm_model])
    parser.add_argument("--top-k", type=int)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--limit", type=int, help="only run the first N questions")
    parser.add_argument("--out", type=Path, help="output folder (default: eval/results/<timestamp>)")
    args = parser.parse_args()

    questions = json.loads(Path(args.questions).read_text(encoding="utf-8"))[: args.limit]
    out_dir = args.out or SOURCE_ROOT / "eval" / "results" / datetime.now().strftime("%Y%m%d-%H%M%S")
    rows: List[dict] = []
    for model in args.models:
        rows += evaluate_model(model, questions, args)
        write_report(rows, out_dir)  # after every model, so a crash late in a long run loses little
    print("\n" + summarise(rows))
    print(f"\nSaved results to {out_dir}")


if __name__ == "__main__":
    main()
