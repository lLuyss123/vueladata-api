FROM python:3.12-slim

# Instalar el binario oficial de uv para gestión ultrarrápida y reproducible de dependencias
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Crear usuario no privilegiado (criterio de seguridad HU-20)
RUN useradd --create-home --home-dir /home/appuser appuser

WORKDIR /code

# Copiar manifiestos de dependencias
COPY pyproject.toml uv.lock ./

# Instalar dependencias exactas del lockfile sin paquetes de desarrollo
RUN uv sync --frozen --no-dev

# Copiar el código fuente de la aplicación
COPY app ./app

# Asignar permisos al usuario no root
RUN chown -R appuser:appuser /code

USER appuser

EXPOSE 8000

# Chequeo de salud del contenedor usando urllib estándar de Python (criterio HU-20)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]