from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.evento_pago import EventoPagoCreate, EventoPagoResponse
from app.schemas.pago import PagoUpdate
import app.crud.evento_pago as crud_evento
import app.crud.pago as crud_pago

router = APIRouter(
    prefix="/eventos-pago",
    tags=["Eventos de Pago"],
)


@router.get(
    "/",
    response_model=list[EventoPagoResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar eventos de pago asíncronos",
    description="Devuelve el historial de respuestas asíncronas recibidas desde la pasarela de pagos F7.",
)
def read_eventos_pago(
    id_pago: int | None = Query(None, description="Filtrar por ID de solicitud de pago"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
):
    return crud_evento.get_eventos_pago(db, id_pago=id_pago, skip=skip, limit=limit)


@router.get(
    "/{id_evento_pago}",
    response_model=EventoPagoResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener evento de pago por ID",
    responses={
        404: {"description": "Evento de pago no encontrado"},
    },
)
def read_evento_pago(
    id_evento_pago: int,
    db: Session = Depends(get_db),
):
    evento = crud_evento.get_evento_pago_by_id(db, id_evento_pago=id_evento_pago)
    if evento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Evento de pago con id {id_evento_pago} no fue encontrado",
        )
    return evento


@router.post(
    "/",
    response_model=EventoPagoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar confirmación asíncrona de pago",
    description="Webhook/consumidor para registrar una confirmación de pago de F7. Actualiza el estado del pago asociado.",
    responses={
        400: {"description": "Evento externo duplicado"},
        404: {"description": "Pago no encontrado"},
    },
)
def create_evento_pago(
    evento_in: EventoPagoCreate,
    db: Session = Depends(get_db),
):
    # Validar que el pago exista
    db_pago = crud_pago.get_pago_by_id(db, id_pago=evento_in.id_pago)
    if db_pago is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el pago con id {evento_in.id_pago}",
        )

    # Validar idempotencia de evento externo
    existing_event = crud_evento.get_evento_pago_by_externo(
        db, id_externo_evento=evento_in.id_externo_evento
    )
    if existing_event:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya se procesó el evento externo '{evento_in.id_externo_evento}'",
        )

    # Crear el evento
    nuevo_evento = crud_evento.create_evento_pago(db, evento_in=evento_in)

    # Actualizar el estado del pago padre para mantener coherencia
    crud_pago.update_pago(
        db,
        db_pago=db_pago,
        pago_in=PagoUpdate(estado=evento_in.estado_reportado),
    )

    return nuevo_evento
