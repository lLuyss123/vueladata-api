FROM python:3.12-slim

# Metadatos de la imagen según infraestructura
LABEL maintainer="VuelaData Team"
LABEL repository="vueladata/backend-workers"
LABEL description="Imagen unificada para FastAPI Backend, Worker RDS, Worker Lake y Producer"

WORKDIR /app

# Crear usuario de sistema sin privilegios (criterio de seguridad ECS/Fargate)
RUN useradd --create-home --home-dir /home/appuser appuser

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente completo
COPY . .

# Permisos para el usuario no root
RUN chown -R appuser:appuser /app
USER appuser

# Variables de entorno por defecto
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV PORT=8000

# Puerto expuesto para cuando corre como FastAPI
EXPOSE 8000

# Comando por defecto: FastAPI Backend
# En ECS Task Definitions se sobrescribe en el campo 'command':
# - Para Worker RDS:  ["python", "-m", "worker_rds.main"]
# - Para Worker Lake: ["python", "-m", "worker_lake.main"]
# - Para Producer:    ["python", "-m", "simulate_stream"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

