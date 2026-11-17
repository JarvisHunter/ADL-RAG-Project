# Demo videos

One screen recording per task (Tasks 1–4), recorded from the running system (real commands and real
model output). The files are 19–34 MB each and git-ignored, so upload them to Canvas or a drive and
put the links in the last column.

| Task | File | Length | What it shows | Link |
|---|---|---|---|---|
| 1. PDF support | `task1.mp4` | 1:09 | `cli.py --data-dir data/docs ingest --rebuild` indexing 3 TXT files + 1 PDF (4 files, 115 chunks, page 10 flagged as image-only); the resulting Chroma database opened to show the chunk text and the `source` / `page` / `file_type` metadata | |
| 2. Handbook chatbot | `task2.mp4` | 1:00 | `cmd_ask` in `cli.py`; `cli.py ask` for the CS minor credits (24) and major credits (56), both cited to `CS_MajorHandbook.pdf p.7` with the retrieved sources; "hello" refused in about 2 s without calling the model | |
| 3. Docker deployment | `task3.mp4` | 1:07 | `docker-compose.yml` and the `Dockerfile`; `docker compose up -d --build`; `docker ps` showing the container as healthy; `docker compose exec rag-app python cli.py ask "What is CS 201 about?"` answered from p.16 | |
| 4. Web UI | `task4.mp4` | 1:51 | Streamlit app on port 8501: settings (model, top-k, temperature, strict mode, sources), indexed files, upload and rebuild controls; "What is the course CS201 about?" with the expanded sources and similarities; "Who is the professor of the course?" refused; a question about total degree credits | |

The recordings use `qwen3.5:0.8b` with `mxbai-embed-large`, served by a self-hosted Ollama server.
