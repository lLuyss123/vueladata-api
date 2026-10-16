from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.causa import CausaCreate, CausaResponse, CausaUpdate
import app.crud.causa as crud_causa

router = APIRouter(
    prefix="/causas",
    tags=["Causas"],
)


@router.get(
    "/",
    response_model=list[CausaResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar todas las causas",
    description="Obtiene el catálogo de causas operacionales con soporte para paginación.",
)
def read_causas(
    skip: int = Query(0, ge=0, description="Número de registros a omitir para paginación"),
    limit: int = Query(100, ge=1, le=200, description="Máximo número de registros a retornar"),
    db: Session = Depends(get_db),
):
    return crud_causa.get_causas(db, skip=skip, limit=limit)


@router.get(
    "/{id_causa}",
    response_model=CausaResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener una causa por ID",
    description="Devuelve la información detallada de una causa según su identificador único.",
    responses={
        404: {"description": "Causa no encontrada"},
    },
)
def read_causa(
    id_causa: int,
    db: Session = Depends(get_db),
):
    causa = crud_causa.get_causa_by_id(db, id_causa=id_causa)
    if causa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Causa con id {id_causa} no fue encontrada",
        )
    return causa


@router.post(
    "/",
    response_model=CausaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva causa",
    description="Registra una nueva causa operacional en el catálogo. Valida unicidad del código.",
    responses={
        400: {"description": "Código de causa duplicado"},
        422: {"description": "Error de validación en los datos enviados"},
    },
)
def create_causa(
    causa_in: CausaCreate,
    db: Session = Depends(get_db),
):
    existing = crud_causa.get_causa_by_codigo(db, codigo=causa_in.codigo)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya existe una causa con el código '{causa_in.codigo}'",
        )
    return crud_causa.create_causa(db, causa_in=causa_in)


@router.patch(
    "/{id_causa}",
    response_model=CausaResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar parcialmente una causa",
    description="Permite modificar uno o varios campos de una causa existente.",
    responses={
        404: {"description": "Causa no encontrada"},
        400: {"description": "Código de causa duplicado"},
    },
)
def update_causa(
    id_causa: int,
    causa_in: CausaUpdate,
    db: Session = Depends(get_db),
):
    db_causa = crud_causa.get_causa_by_id(db, id_causa=id_causa)
    if db_causa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Causa con id {id_causa} no fue encontrada",
        )
    if causa_in.codigo and causa_in.codigo != db_causa.codigo:
        conflict = crud_causa.get_causa_by_codigo(db, codigo=causa_in.codigo)
        if conflict:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe otra causa con el código '{causa_in.codigo}'",
            )
    return crud_causa.update_causa(db, db_causa=db_causa, causa_in=causa_in)


@router.delete(
    "/{id_causa}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una causa",
    description="Elimina una causa del catálogo operacional.",
    responses={
        404: {"description": "Causa no encontrada"},
    },
)
def delete_causa(
    id_causa: int,
    db: Session = Depends(get_db),
):
    db_causa = crud_causa.get_causa_by_id(db, id_causa=id_causa)
    if db_causa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Causa con id {id_causa} no fue encontrada",
        )
    crud_causa.delete_causa(db, db_causa=db_causa)
    return None