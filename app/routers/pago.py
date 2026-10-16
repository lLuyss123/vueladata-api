from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.pago import PagoCreate, PagoResponse, PagoUpdate
import app.crud.pago as crud_pago
import app.crud.compensacion as crud_comp

router = APIRouter(
    prefix="/pagos",
    tags=["Pagos"],
)


@router.get(
    "/",
    response_model=list[PagoResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar solicitudes de pago",
    description="Devuelve las solicitudes de pago de compensaciones registradas hacia la pasarela F7.",
)
def read_pagos(
    estado: str | None = Query(None, description="Filtrar por estado: PENDIENTE, PAGADO, RECHAZADO"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return crud_pago.get_pagos(db, skip=skip, limit=limit, estado=estado)


@router.get(
    "/{id_pago}",
    response_model=PagoResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener pago por ID",
    responses={
        404: {"description": "Pago no encontrado"},
    },
)
def read_pago(
    id_pago: int,
    db: Session = Depends(get_db),
):
    pago = crud_pago.get_pago_by_id(db, id_pago=id_pago)
    if pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pago con id {id_pago} no fue encontrado",
        )
    return pago


@router.get(
    "/idempotencia/{clave_idempotencia}",
    response_model=PagoResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar pago por clave de idempotencia",
    description="Permite recuperar un pago previamente iniciado utilizando su clave única de idempotencia.",
    responses={
        404: {"description": "Pago no encontrado para la clave de idempotencia proporcionada"},
    },
)
def read_pago_by_idempotencia(
    clave_idempotencia: str,
    db: Session = Depends(get_db),
):
    pago = crud_pago.get_pago_by_clave_idempotencia(db, clave_idempotencia=clave_idempotencia)
    if pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontró ningún pago con clave de idempotencia '{clave_idempotencia}'",
        )
    return pago


@router.post(
    "/",
    response_model=PagoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Iniciar solicitud de pago",
    description="Crea una solicitud de pago. Valida la clave de idempotencia y que la compensación no tenga otro pago (RN-09).",
    responses={
        400: {"description": "Clave de idempotencia duplicada o compensación ya pagada"},
        404: {"description": "Compensación no encontrada"},
    },
)
def create_pago(
    pago_in: PagoCreate,
    db: Session = Depends(get_db),
):
    # Validar que la compensación exista
    comp = crud_comp.get_compensacion_by_id(db, id_compensacion=pago_in.id_compensacion)
    if comp is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La compensación con id {pago_in.id_compensacion} no existe",
        )

    # Validar clave de idempotencia única
    existing_idempotency = crud_pago.get_pago_by_clave_idempotencia(
        db, clave_idempotencia=pago_in.clave_idempotencia
    )
    if existing_idempotency:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya existe una solicitud de pago con la clave de idempotencia '{pago_in.clave_idempotencia}'",
        )

    # Validar que la compensación no tenga ya un pago (RN-09)
    existing_payment = crud_pago.get_pago_by_compensacion(db, id_compensacion=pago_in.id_compensacion)
    if existing_payment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La compensación {pago_in.id_compensacion} ya tiene un pago registrado (id_pago: {existing_payment.id_pago}) (RN-09)",
        )

    return crud_pago.create_pago(db, pago_in=pago_in)


@router.patch(
    "/{id_pago}",
    response_model=PagoResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar estado de pago",
    description="Actualiza el estado y/o la transacción externa devuelta por la pasarela de pagos.",
    responses={
        404: {"description": "Pago no encontrado"},
    },
)
def update_pago(
    id_pago: int,
    pago_in: PagoUpdate,
    db: Session = Depends(get_db),
):
    db_pago = crud_pago.get_pago_by_id(db, id_pago=id_pago)
    if db_pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pago con id {id_pago} no fue encontrado",
        )
    return crud_pago.update_pago(db, db_pago=db_pago, pago_in=pago_in)


@router.delete(
    "/{id_pago}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar pago",
    responses={
        404: {"description": "Pago no encontrado"},
    },
)
def delete_pago(
    id_pago: int,
    db: Session = Depends(get_db),
):
    db_pago = crud_pago.get_pago_by_id(db, id_pago=id_pago)
    if db_pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pago con id {id_pago} no fue encontrado",
        )
    crud_pago.delete_pago(db, db_pago=db_pago)
    return None
