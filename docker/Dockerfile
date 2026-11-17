# Handbook RAG chatbot (Streamlit UI + CLI).
# Build from the repository root:
#   docker build -f docker/Dockerfile -t handbook-rag .
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    OLLAMA_BASE_URL=http://host.docker.internal:11434 \
    RAG_DATA_DIR=/app/data/docs \
    RAG_VECTOR_STORE_DIR=/app/vector_store

WORKDIR /app

COPY source_code/requirements.txt .
RUN pip install -r requirements.txt

COPY source_code/ .

RUN useradd --create-home --uid 1000 rag \
    && mkdir -p /app/vector_store \
    && chown -R rag:rag /app
USER rag

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')" || exit 1

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true", "--browser.gatherUsageStats=false"]
