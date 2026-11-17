# Local RAG Chatbot for the FUV Computer Science Major Handbook

A fully local Retrieval-Augmented Generation (RAG) system that answers questions about PDF and text
documents, built for the CS311 Advanced Deep Learning final project. Documents are chunked,
embedded with an Ollama embedding model, stored in ChromaDB, and answered by a local LLM served by
Ollama. 

```
Documents (PDF/TXT) ──► pypdf + cleaning ──► chunks ──► embeddings ──► ChromaDB
                                                                         │ top-k
User question (+ chat history) ─────────────────────────────────────────►│
                                                                         ▼
                                            prompt (context + history) ──► Ollama LLM ──► answer + sources
```

## Features

| Task | What is implemented | Where |
|---|---|---|
| 1. PDF support | Page-level PDF extraction with `pypdf`, text cleaning (ligatures, hyphenation, TOC dot leaders), page numbers kept as metadata, image-only pages reported | [`source_code/rag/loaders.py`](source_code/rag/loaders.py) |
| 2. Handbook chatbot | CS major handbook indexed by default; 27 test questions across requirements, courses, outcomes, policies, ambiguous, out-of-scope, off-topic and multi-turn follow-up cases; evaluation script with multi-model comparison; retrieval experiment over chunk size and embedding model | [`source_code/eval/`](source_code/eval), [`source_code/evaluate.py`](source_code/evaluate.py) |
| 3. Docker | `Dockerfile` + `docker-compose.yml`, mounted documents, persistent vector-store volume, health check | [`docker/`](docker) |
| 4. Web UI | Streamlit chat with conversation history, streaming answers, cited sources with similarity scores, model/top-k/temperature controls, document upload, index rebuild, chat export | [`source_code/app.py`](source_code/app.py) |



## Repository layout

```
.
├── source_code/
│   ├── rag/                 # the RAG library
│   │   ├── config.py        # settings (env vars / .env)
│   │   ├── loaders.py       # TXT/MD/PDF loading + cleaning
│   │   ├── indexer.py       # chunking, embeddings, Chroma, manifest
│   │   ├── prompts.py       # prompt templates
│   │   ├── pipeline.py      # retrieve -> prompt -> generate
│   │   └── models.py        # Ollama model factories + health check
│   ├── app.py               # Streamlit web UI
│   ├── cli.py               # command-line interface
│   ├── evaluate.py          # batch evaluation for the report
│   ├── retrieval_sweep.py   # retrieval-only experiment (chunk size x embedding model)
│   ├── eval/cs_handbook_questions.json
│   ├── data/docs/           # CS_MajorHandbook.pdf + mixed TXT/PDF documents
│   ├── tests/               # pytest suite (runs without Ollama)
│   └── requirements.txt
├── docker/                  # Dockerfile, docker-compose.yml
├── report/                  # final report PDF (Task 5)
├── demo_video/              # demo videos or links (Task 6)
└── sample_code/             # original baseline from the course
```

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/download) with an embedding model and a chat model:
  ```bash
  ollama pull nomic-embed-text
  ollama pull qwen2.5:0.5b      # optionally also qwen2.5:1.5b, qwen2.5:3b
  ```
- Docker (for Task 3)

## Installation

```bash
conda create -n rag python=3.10
conda activate rag
cd source_code
pip install -r requirements.txt
cp .env.example .env            # optional: change models, paths, top-k, ...
```

## Usage

All commands are run from `source_code/`. Make sure `ollama serve` is running.

```bash
python cli.py check                                   # Ollama reachable? models pulled?
python cli.py ingest                                  # build the vector store (auto-skipped if unchanged)
python cli.py ask "What are the prerequisites for CS 302?"
python cli.py ask "What GPA is needed for the capstone?" --show-context
python cli.py chat                                    # interactive chat with history (/clear, /exit)
```

Global options go before the sub-command, e.g.:

```bash
python cli.py --model qwen2.5:1.5b --top-k 8 ask "List the advanced CS courses"
python cli.py --data-dir data/docs ingest --rebuild   # Task 1: index a folder of TXT + PDF files
```

> The index is rebuilt automatically when the document folder changes. To keep both indexes, give
> each folder its own store, e.g. `--data-dir data/docs --vector-store vector_store_docs`.

### Web interface

```bash
streamlit run app.py          # http://localhost:8501
```

### Evaluation (Task 2)

```bash
python evaluate.py                                          # default model
python evaluate.py --models qwen2.5:0.5b qwen2.5:1.5b qwen2.5:3b
```

Results are written to `eval/results/<timestamp>/` as `results.csv`, `results.json` and `summary.md`.
Each row contains the answer, retrieved pages, whether an expected page was retrieved, a keyword
score, whether the model refused, and latency. The `label` column is left empty for manual grading
(correct / incorrect / incomplete / ambiguous) to use in the report. A question can list earlier
turns under `"history"`; they are asked first, so follow-up questions are tested with real chat history.

The labelled run used in the report is kept in [`eval/results/final/`](source_code/eval/results/final)
(`labels_summary.md` has the per-model counts).

Results of that run (strict mode, `mxbai-embed-large`, 1,000/200 chunks, top-5, temperature 0.2;
every answer labelled by hand):

| Model | Answerable questions correct | Correct refusals | Mean latency* |
|---|---|---|---|
| qwen3.5:9b | 20/23 | 4/4 | 17.8 s |
| gemma3:4b | 19/23 | 4/4 | 11.3 s |
| llama3.2:3b | 18/23 | 4/4 | 9.4 s |
| qwen2.5:3b | 16/23 | 4/4 | 7.3 s |
| qwen3.5:0.8b | 12/23 | 4/4 | 9.6 s |
| qwen2.5:0.5b-instruct | 10/23 | 2/4 | 6.6 s |

\*Shared remote GPU server; indicative only. Retrieval found an expected page for 22 of 23 questions.
See the report for the error analysis and the before/after comparison of the strict-mode fixes.

Retrieval only (no LLM), comparing chunk sizes and embedding models:

```bash
python retrieval_sweep.py --embed-models mxbai-embed-large qwen3-embedding:8b --chunk-sizes 500 1000 1500
```

### Tests

```bash
pytest -q          # uses fake embeddings/LLM, no Ollama required
```

## Docker deployment

Ollama runs on the host; the container connects to it via `host.docker.internal`.

```bash
cd docker
cp .env.example .env                 # optional
docker compose up --build            # open http://localhost:8501
```

Useful commands:

```bash
docker compose run --rm rag-app python cli.py check
docker compose run --rm rag-app python cli.py ingest --rebuild
docker compose run --rm rag-app python cli.py ask "How many credits does the CS minor require?"
docker compose down                  # add -v to delete the vector-store volume
```

Without compose:

```bash
docker build -f docker/Dockerfile -t handbook-rag .
docker run --rm -p 8501:8501 \
  --add-host host.docker.internal:host-gateway \
  -v "$(pwd)/source_code/data:/app/data" \
  handbook-rag
```

- Documents are mounted from `source_code/data`, so new PDFs need no image rebuild.
- The vector store lives in the `rag_vector_store` volume and survives restarts.
- On Linux, Ollama must listen on all interfaces for the container to reach it
  (`OLLAMA_HOST=0.0.0.0 ollama serve`).

## Configuration

All settings can be set as environment variables or in `source_code/.env`
(see [`.env.example`](source_code/.env.example)).

| Variable | Default | Meaning |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://127.0.0.1:11434` | Ollama server (a trailing `/v1` is ignored) |
| `OLLAMA_API_KEY` | _(empty)_ | bearer token for a protected Ollama server; `LLM_API_KEY` is also accepted |
| `RAG_LLM_MODEL` | `qwen2.5:0.5b` | chat model |
| `RAG_EMBED_MODEL` | `nomic-embed-text` | embedding model |
| `RAG_THINK` | `false` | let "thinking" models (qwen3, qwen3.5, deepseek-r1) reason before answering; off because small ones can reason for minutes and return nothing |
| `RAG_MAX_TOKENS` | `1024` | max tokens generated per answer |
| `RAG_NUM_CTX` | `8192` | context window requested from Ollama |
| `RAG_REQUEST_TIMEOUT` | `180` | seconds before an Ollama request is abandoned |
| `RAG_DATA_DIR` | `data/docs` | folder of documents to index |
| `RAG_VECTOR_STORE_DIR` | `vector_store` | Chroma persistence folder |
| `RAG_CHUNK_SIZE` / `RAG_CHUNK_OVERLAP` | `1000` / `200` | chunking (characters) |
| `RAG_TOP_K` | `5` | chunks retrieved per question |
| `RAG_SCORE_THRESHOLD` | _(auto)_ | minimum cosine similarity to keep a chunk; unset = 0.55 for `mxbai-embed-large`, 0.3 for other models |
| `RAG_ALLOW_GENERAL_KNOWLEDGE` | `false` | allow answers from model knowledge |
| `RAG_TEMPERATURE` | `0.2` | sampling temperature |
| `RAG_HISTORY_TURNS` | `3` | previous Q/A pairs sent to the model |
