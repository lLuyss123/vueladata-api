from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class EventoPagoBase(BaseModel):
    id_pago: int = Field(...)
    id_externo_evento: str = Field(..., max_length=150, min_length=1)
    estado_reportado: Literal['PENDIENTE', 'PAGADO', 'RECHAZADO'] = Field(..., max_length=30)
    fecha_hora_evento_utc: datetime = Field(...)
    fecha_hora_recepcion_utc: datetime = Field(...)


class EventoPagoCreate(EventoPagoBase):
    pass


class EventoPagoUpdate(BaseModel):
    id_pago: int | None = Field(default=None)
    id_externo_evento: str | None = Field(default=None, max_length=150, min_length=1)
    estado_reportado: Literal['PENDIENTE', 'PAGADO', 'RECHAZADO'] | None = Field(default=None, max_length=30)
    fecha_hora_evento_utc: datetime | None = Field(default=None)
    fecha_hora_recepcion_utc: datetime | None = Field(default=None)


class EventoPagoResponse(EventoPagoBase):
    id_evento_pago: int
    model_config = ConfigDict(from_attributes=True)

