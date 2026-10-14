from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class PagoBase(BaseModel):
    id_compensacion: int = Field(...)
    clave_idempotencia: str = Field(..., max_length=150, min_length=1)
    id_transaccion_externa: str | None = Field(default=None, max_length=150)
    estado: Literal['PENDIENTE', 'PAGADO', 'RECHAZADO'] = Field(..., max_length=30)
    fecha_solicitud_utc: datetime = Field(...)
    fecha_actualizacion_utc: datetime = Field(...)


class PagoCreate(PagoBase):
    pass


class PagoUpdate(BaseModel):
    id_compensacion: int | None = Field(default=None)
    clave_idempotencia: str | None = Field(default=None, max_length=150, min_length=1)
    id_transaccion_externa: str | None = Field(default=None, max_length=150)
    estado: Literal['PENDIENTE', 'PAGADO', 'RECHAZADO'] | None = Field(default=None, max_length=30)
    fecha_solicitud_utc: datetime | None = Field(default=None)
    fecha_actualizacion_utc: datetime | None = Field(default=None)


class PagoResponse(PagoBase):
    id_pago: int
    model_config = ConfigDict(from_attributes=True)

