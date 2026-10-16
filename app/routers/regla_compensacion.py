from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.regla_compensacion import (
    ReglaCompensacionCreate,
    ReglaCompensacionResponse,
    ReglaCompensacionUpdate,
)
import app.crud.regla_compensacion as crud_regla

router = APIRouter(
    prefix="/reglas-compensacion",
    tags=["Reglas de Compensación"],
)


@router.get(
    "/",
    response_model=list[ReglaCompensacionResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar reglas de compensación",
    description="Devuelve las reglas de cálculo de compensaciones económicas (RN-05).",
)
def read_reglas_compensacion(
    tipo_incidencia: str | None = Query(None, description="Filtrar por 'RETRASO' o 'CANCELACION'"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return crud_regla.get_reglas_compensacion(db, skip=skip, limit=limit, tipo_incidencia=tipo_incidencia)


@router.get(
    "/{id_regla_compensacion}",
    response_model=ReglaCompensacionResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener regla por ID",
    responses={
        404: {"description": "Regla no encontrada"},
    },
)
def read_regla_compensacion(
    id_regla_compensacion: int,
    db: Session = Depends(get_db),
):
    regla = crud_regla.get_regla_compensacion_by_id(db, id_regla=id_regla_compensacion)
    if regla is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Regla de compensación con id {id_regla_compensacion} no fue encontrada",
        )
    return regla


@router.post(
    "/",
    response_model=ReglaCompensacionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear regla de compensación",
)
def create_regla_compensacion(
    regla_in: ReglaCompensacionCreate,
    db: Session = Depends(get_db),
):
    return crud_regla.create_regla_compensacion(db, regla_in=regla_in)


@router.patch(
    "/{id_regla_compensacion}",
    response_model=ReglaCompensacionResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar regla de compensación",
    responses={
        404: {"description": "Regla no encontrada"},
    },
)
def update_regla_compensacion(
    id_regla_compensacion: int,
    regla_in: ReglaCompensacionUpdate,
    db: Session = Depends(get_db),
):
    db_regla = crud_regla.get_regla_compensacion_by_id(db, id_regla=id_regla_compensacion)
    if db_regla is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Regla de compensación con id {id_regla_compensacion} no fue encontrada",
        )
    return crud_regla.update_regla_compensacion(db, db_regla=db_regla, regla_in=regla_in)


@router.delete(
    "/{id_regla_compensacion}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar regla de compensación",
    responses={
        404: {"description": "Regla no encontrada"},
    },
)
def delete_regla_compensacion(
    id_regla_compensacion: int,
    db: Session = Depends(get_db),
):
    db_regla = crud_regla.get_regla_compensacion_by_id(db, id_regla=id_regla_compensacion)
    if db_regla is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Regla de compensación con id {id_regla_compensacion} no fue encontrada",
        )
    crud_regla.delete_regla_compensacion(db, db_regla=db_regla)
    return None
