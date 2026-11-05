#!/usr/bin/env bash
# ==============================================================================
# SCRIPT BASH DE DESPLIEGUE A AMAZON ECR: vueladata/backend-workers
# ==============================================================================
# Uso:
#   ./deploy_ecr.sh <ACCOUNT_ID> [REGION]
# ==============================================================================

set -euo pipefail

ACCOUNT_ID="${1:-}"
REGION="${2:-us-east-1}"
REPO_NAME="vueladata/backend-workers"
IMAGE_TAG="latest"

if [ -z "$ACCOUNT_ID" ]; then
    echo "❌ Error: Debes proporcionar el AWS Account ID como primer parámetro."
    echo "Uso: ./deploy_ecr.sh <ACCOUNT_ID> [REGION]"
    exit 1
fi

ECR_URI="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPO_NAME}"

echo "=========================================================="
echo "🚀 Desplegando en ECR: ${ECR_URI}:${IMAGE_TAG}"
echo "=========================================================="

echo -e "\n[1/4] Login en ECR..."
aws ecr get-login-password --region "${REGION}" | docker login --username AWS --password-stdin "${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"

echo -e "\n[2/4] Compilando imagen para Linux amd64 (ECS Fargate)..."
docker build --platform linux/amd64 -t "${REPO_NAME}:${IMAGE_TAG}" .

echo -e "\n[3/4] Etiquetando imagen..."
docker tag "${REPO_NAME}:${IMAGE_TAG}" "${ECR_URI}:${IMAGE_TAG}"

echo -e "\n[4/4] Subiendo imagen a ECR..."
docker push "${ECR_URI}:${IMAGE_TAG}"

echo -e "\n✅ ¡Listo! Imagen disponible en Amazon ECR."

