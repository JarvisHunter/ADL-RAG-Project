#!/usr/bin/env python3
"""Command-line interface for the local RAG system.

Usage:
    python cli.py check                          # is Ollama reachable, are models pulled?
    python cli.py ingest [--rebuild]             # build / refresh the vector store
    python cli.py ask "What is CS 201 about?"    # one question
    python cli.py chat                           # interactive chat with history

Common options (before the sub-command):
    --data-dir PATH   folder of .pdf/.txt/.md documents (default: data/docs)
    --model NAME      Ollama LLM, e.g. qwen2.5:1.5b
    --top-k N         number of chunks to retrieve
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from rag import RAGPipeline, get_settings
from rag.models import check_ollama

DEFAULT_QUESTION = "How many credits are required for the Computer Science major?"


def build_settings(args: argparse.Namespace):
    return get_settings(
        data_dir=Path(args.data_dir).resolve() if args.data_dir else None,
        vector_store_dir=Path(args.vector_store).resolve() if args.vector_store else None,
        llm_model=args.model,
        embed_model=args.embed_model,
        top_k=args.top_k,
        temperature=args.temperature,
        allow_general_knowledge=True if args.general_knowledge else None,
    )


def print_response(response, show_context: bool = False) -> None:
    print(f"\nA: {response.answer}\n")
    if response.used_fallback:
        print("(no sufficiently relevant passages were retrieved)")
    else:
        print("Sources:")
        for chunk in response.sources:
            print(f"  - {chunk.label}  score={chunk.score:.3f}")
            if show_context:
                print("    " + chunk.content[:400].replace("\n", " ") + " ...")
    print(f"({response.latency_s:.2f}s)")


def cmd_check(settings) -> int:
    status = check_ollama(settings)
    if not status["reachable"]:
        print(status["error"])
        return 1
    print(f"Ollama OK at {settings.ollama_base_url}")
    print("Pulled models: " + (", ".join(status["models"]) or "(none)"))
    for name in status["missing"]:
        print(f"Missing model: {name}  ->  ollama pull {name}")
    return 1 if status["missing"] else 0


def cmd_ingest(settings, rebuild: bool) -> int:
    pipeline = RAGPipeline(settings)
    stats = pipeline.ensure_index(force=rebuild)
    action = "Rebuilt" if stats["rebuilt"] else "Reused"
    print(f"{action} index: {stats['files']} file(s), {stats['chunks']} chunk(s) -> {settings.vector_store_dir}")
    return 0


def cmd_ask(settings, question: str, show_context: bool) -> int:
    pipeline = RAGPipeline(settings)
    pipeline.ensure_index()
    print(f"Q: {question}")
    print_response(pipeline.ask(question), show_context)
    return 0


def cmd_chat(settings, show_context: bool) -> int:
    pipeline = RAGPipeline(settings)
    pipeline.ensure_index()
    history = []
    print(f"Chatting with {settings.llm_model} over {settings.data_dir}. Commands: /clear, /exit")
    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not question:
            continue
        if question in {"/exit", "/quit"}:
            return 0
        if question == "/clear":
            history.clear()
            print("(history cleared)")
            continue
        response = pipeline.ask(question, history)
        print_response(response, show_context)
        history += [{"role": "user", "content": question}, {"role": "assistant", "content": response.answer}]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Local RAG chatbot (PDF/TXT documents + Ollama)")
    parser.add_argument("--data-dir", help="folder with .pdf/.txt/.md documents")
    parser.add_argument("--vector-store", help="folder where Chroma persists vectors")
    parser.add_argument("--model", help="Ollama chat model, e.g. qwen2.5:0.5b")
    parser.add_argument("--embed-model", help="Ollama embedding model, e.g. nomic-embed-text")
    parser.add_argument("--top-k", type=int, help="number of chunks to retrieve")
    parser.add_argument("--temperature", type=float)
    parser.add_argument("--general-knowledge", action="store_true", help="allow answers from model knowledge")
    parser.add_argument("-v", "--verbose", action="store_true")

    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="check Ollama connection and models")
    p_ingest = sub.add_parser("ingest", help="build the vector store")
    p_ingest.add_argument("--rebuild", action="store_true", help="force a full rebuild")
    p_ask = sub.add_parser("ask", help="ask one question")
    p_ask.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    p_ask.add_argument("--show-context", action="store_true")
    p_chat = sub.add_parser("chat", help="interactive chat")
    p_chat.add_argument("--show-context", action="store_true")

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s %(message)s")
    # One "HTTP Request: POST .../api/embed" line per Ollama call drowns out the useful -v output.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    settings = build_settings(args)

    if args.command == "check":
        return cmd_check(settings)
    if args.command == "ingest":
        return cmd_ingest(settings, args.rebuild)
    if args.command == "ask":
        return cmd_ask(settings, args.question, args.show_context)
    return cmd_chat(settings, args.show_context)


if __name__ == "__main__":
    sys.exit(main())
