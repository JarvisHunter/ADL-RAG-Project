# Demo videos

One video per task (Tasks 1–4), 1280×720 H.264, recorded from the running system (real commands
and real model output, no editing). Captions on screen explain each step. The files are small
(2–3 MB each); they are git-ignored by default, so upload them to Canvas or a drive and put the
links in the last column.

| Task | File | Length | What it shows | Link |
|---|---|---|---|---|
| 1. PDF support | `task1_pdf_support.mp4` | 2:23 | Baseline `*.txt` loader vs. new PDF loader; indexing a folder of 3 TXT files + 1 PDF; questions answered from the PDF (with page citations and `--show-context`) and from a TXT file | |
| 2. Handbook chatbot | `task2_handbook_chatbot.mp4` | 3:38 | CS handbook indexing; the same question answered wrongly by qwen3.5:0.8b and correctly by gemma3:4b; a policy question with a citation; interactive chat with a follow-up and an off-topic question; `evaluate.py`; the labelled 6-model results | |
| 3. Docker deployment | `task3_docker.mp4` | 1:57 | Dockerfile and compose file; `docker compose up -d --build`; health check; CLI inside the container; persistent volume; the web UI served from the container; `docker compose down` | |
| 4. Web UI | `task4_web_ui.mp4` | 2:53 | Streamlit chat: example questions, streamed answers, sources with similarity, conversation history, off-topic refusal, model switch, PDF upload, export and clear | |

The recordings use `qwen3.5:0.8b` by default (`gemma3:4b` in Task 2 and `qwen2.5:3b` in the Task 4 model-switch step) with
`mxbai-embed-large`, served by a self-hosted Ollama server.
