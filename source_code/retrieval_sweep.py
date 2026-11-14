#!/usr/bin/env python3
"""Retrieval-only experiment: how chunk size and embedding model affect retrieval.

No language model is involved. For every (embedding model, chunk size) pair the handbook is indexed
into a throw-away vector store, every answerable test question is retrieved, and we measure

- hit@k: an expected handbook page is among the top-k chunks (k = 1, 3, 5)
- MRR:   mean reciprocal rank of the first chunk from an expected page
- the top-1 similarity of handbook questions vs. off-topic questions (to choose a score threshold)

Usage:
    python retrieval_sweep.py
    python retrieval_sweep.py --embed-models mxbai-embed-large nomic-embed-text --chunk-sizes 500 1000 1500
"""

from __future__ import annotations

import argparse
import json
import statistics
import tempfile
from pathlib import Path

from rag import get_settings
from rag.config import SOURCE_ROOT
from rag.indexer import VectorIndex
from rag.models import get_embeddings

KS = (1, 3, 5)


def evaluate(embed_model: str, chunk_size: int, questions: list, store_root: Path) -> dict:
    settings = get_settings(
        embed_model=embed_model,
        chunk_size=chunk_size,
        chunk_overlap=chunk_size // 5,
        vector_store_dir=store_root / f"{embed_model.replace(':', '_')}_{chunk_size}",
    )
    index = VectorIndex(settings, get_embeddings(settings))
    stats = index.build(force=True)

    ranks, in_scope, off_topic = [], [], []
    for item in questions:
        results = index.store.similarity_search_with_score(item["question"], k=max(KS))
        top1 = 1.0 - float(results[0][1]) if results else 0.0
        if item["category"] == "off_topic":
            off_topic.append(top1)
            continue
        if item.get("history") or not item.get("pages"):
            continue  # follow-ups need the chat history; unanswerable ones have no page
        in_scope.append(top1)
        pages = set(item["pages"])
        rank = next((i for i, (doc, _) in enumerate(results, 1) if doc.metadata.get("page") in pages), None)
        ranks.append(rank)

    row = {"embed_model": embed_model, "chunk_size": chunk_size, "chunks": stats["chunks"], "questions": len(ranks)}
    for k in KS:
        row[f"hit@{k}"] = round(sum(r is not None and r <= k for r in ranks) / len(ranks), 3)
    row["mrr"] = round(statistics.mean(1 / r if r else 0 for r in ranks), 3)
    row["top1_in_scope_min"] = round(min(in_scope), 3)
    row["top1_in_scope_mean"] = round(statistics.mean(in_scope), 3)
    row["top1_off_topic_max"] = round(max(off_topic), 3) if off_topic else None
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--questions", default=str(SOURCE_ROOT / "eval" / "cs_handbook_questions.json"))
    parser.add_argument("--embed-models", nargs="+", default=["mxbai-embed-large", "qwen3-embedding:8b"])
    parser.add_argument("--chunk-sizes", nargs="+", type=int, default=[500, 1000, 1500])
    parser.add_argument("--out", type=Path, help="write the rows as JSON here")
    args = parser.parse_args()

    questions = json.loads(Path(args.questions).read_text(encoding="utf-8"))
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for model in args.embed_models:
            for size in args.chunk_sizes:
                rows.append(evaluate(model, size, questions, Path(tmp)))
                print(rows[-1], flush=True)

    header = ["embed_model", "chunk_size", "chunks", "hit@1", "hit@3", "hit@5", "mrr",
              "top1_in_scope_min", "top1_in_scope_mean", "top1_off_topic_max"]
    print("\n| " + " | ".join(header) + " |\n|" + "---|" * len(header))
    for row in rows:
        print("| " + " | ".join(str(row[h]) for h in header) + " |")
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(rows, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
