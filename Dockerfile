# Estágio 1: Build & Dependências (Lightweight)
FROM python:3.10-slim-bullseye AS builder

WORKDIR /app

# Instalar uv para gestão rápida de pacotes
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Instalar dependências sem gerar cache
COPY pyproject.toml .
RUN uv pip install --system --no-cache -r pyproject.toml

# Estágio 2: Runtime (Produção)
FROM python:3.10-slim-bullseye

WORKDIR /app

# Copiar bibliotecas instaladas no estágio anterior
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar o código fonte e artefatos necessários
COPY src/ /app/src/
COPY models/ /app/models/
COPY Makefile /app/

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expor a porta do FastAPI
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
