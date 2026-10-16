from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.compensacion import (
    CompensacionCreate,
    CompensacionResponse,
    CompensacionUpdate,
)
import app.crud.compensacion as crud_comp

router = APIRouter(
    prefix="/compensaciones",
    tags=["Compensaciones"],
)


@router.get(
    "/",
    response_model=list[CompensacionResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar compensaciones económicas",
    description="Obtiene las compensaciones calculadas para pasajeros y segmentos afectados.",
)
def read_compensaciones(
    estado: str | None = Query(None, description="Filtrar por estado (CALCULADA, SOLICITADA, PAGADA, RECHAZADA, ANULADA)"),
    id_detalle_reserva: int | None = Query(None, description="Filtrar por segmento de reserva"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return crud_comp.get_compensaciones(
        db, skip=skip, limit=limit, estado=estado, id_detalle_reserva=id_detalle_reserva
    )


@router.get(
    "/{id_compensacion}",
    response_model=CompensacionResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener compensación por ID",
    responses={
        404: {"description": "Compensación no encontrada"},
    },
)
def read_compensacion(
    id_compensacion: int,
    db: Session = Depends(get_db),
):
    comp = crud_comp.get_compensacion_by_id(db, id_compensacion=id_compensacion)
    if comp is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Compensación con id {id_compensacion} no fue encontrada",
        )
    return comp


@router.post(
    "/",
    response_model=CompensacionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear compensación económica",
    description="Registra una nueva compensación. Valida que el segmento de reserva no tenga una compensación previa (RN-09).",
    responses={
        400: {"description": "El segmento de reserva ya tiene una compensación registrada (RN-09)"},
    },
)
def create_compensacion(
    comp_in: CompensacionCreate,
    db: Session = Depends(get_db),
):
    existing = crud_comp.get_compensacion_by_detalle_reserva(
        db, id_detalle_reserva=comp_in.id_detalle_reserva
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El detalle_reserva {comp_in.id_detalle_reserva} ya tiene la compensación {existing.id_compensacion} asignada (RN-09)",
        )
    return crud_comp.create_compensacion(db, comp_in=comp_in)


@router.patch(
    "/{id_compensacion}",
    response_model=CompensacionResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar compensación",
    responses={
        404: {"description": "Compensación no encontrada"},
    },
)
def update_compensacion(
    id_compensacion: int,
    comp_in: CompensacionUpdate,
    db: Session = Depends(get_db),
):
    db_comp = crud_comp.get_compensacion_by_id(db, id_compensacion=id_compensacion)
    if db_comp is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Compensación con id {id_compensacion} no fue encontrada",
        )
    return crud_comp.update_compensacion(db, db_comp=db_comp, comp_in=comp_in)


@router.delete(
    "/{id_compensacion}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar compensación",
    responses={
        404: {"description": "Compensación no encontrada"},
    },
)
def delete_compensacion(
    id_compensacion: int,
    db: Session = Depends(get_db),
):
    db_comp = crud_comp.get_compensacion_by_id(db, id_compensacion=id_compensacion)
    if db_comp is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Compensación con id {id_compensacion} no fue encontrada",
        )
    crud_comp.delete_compensacion(db, db_comp=db_comp)
    return None
