# ==============================================================================
# SCRIPT DE DESPLIEGUE A AMAZON ECR: vueladata/backend-workers
# ==============================================================================
# Uso:
#   .\deploy_ecr.ps1 -AwsAccountId "123456789012" -Region "us-east-1"
# ==============================================================================

param (
    [Parameter(Mandatory=$true)]
    [string]$AwsAccountId,

    [Parameter(Mandatory=$false)]
    [string]$Region = "us-east-1",

    [Parameter(Mandatory=$false)]
    [string]$RepoName = "vueladata/backend-workers",

    [Parameter(Mandatory=$false)]
    [string]$ImageTag = "latest"
)

$ErrorActionPreference = "Stop"

$EcrUri = "$AwsAccountId.dkr.ecr.$Region.amazonaws.com/$RepoName"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "🚀 Iniciando despliegue hacia Amazon ECR: $EcrUri:$ImageTag" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Autenticación con Amazon ECR
Write-Host "`n[1/4] Autenticando Docker con Amazon ECR..." -ForegroundColor Yellow
aws ecr get-login-password --region $Region | docker login --username AWS --password-stdin "$AwsAccountId.dkr.ecr.$Region.amazonaws.com"

# 2. Construcción de la imagen multiplataforma (Linux amd64 para Fargate)
Write-Host "`n[2/4] Compilando imagen Docker (linux/amd64)..." -ForegroundColor Yellow
docker build --platform linux/amd64 -t "${RepoName}:${ImageTag}" .

# 3. Etiquetado para ECR
Write-Host "`n[3/4] Etiquetando imagen para ECR..." -ForegroundColor Yellow
docker tag "${RepoName}:${ImageTag}" "${EcrUri}:${ImageTag}"

# 4. Push al repositorio ECR
Write-Host "`n[4/4] Subiendo imagen a ECR..." -ForegroundColor Yellow
docker push "${EcrUri}:${ImageTag}"

Write-Host "`n==========================================================" -ForegroundColor Green
Write-Host "✅ Imagen desplegada con éxito en ECR: ${EcrUri}:${ImageTag}" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green

