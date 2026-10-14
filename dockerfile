FROM python:3.12-slim
# Trae el binario de uv desde su imagen oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /code
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev   # instala exactamente lo del lockfile

COPY app ./app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]