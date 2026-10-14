from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class ReubicacionBase(BaseModel):
    id_detalle_reserva: int = Field(...)
    id_incidencia: int = Field(...)
    id_vuelo_propuesto: int | None = Field(default=None)
    estado: Literal['PENDIENTE', 'OFRECIDA', 'ACEPTADA', 'RECHAZADA', 'COMPLETADA'] = Field(..., max_length=30)
    fecha_oferta_utc: datetime | None = Field(default=None)
    fecha_respuesta_utc: datetime | None = Field(default=None)


class ReubicacionCreate(ReubicacionBase):
    pass


class ReubicacionUpdate(BaseModel):
    id_detalle_reserva: int | None = Field(default=None)
    id_incidencia: int | None = Field(default=None)
    id_vuelo_propuesto: int | None = Field(default=None)
    estado: Literal['PENDIENTE', 'OFRECIDA', 'ACEPTADA', 'RECHAZADA', 'COMPLETADA'] | None = Field(default=None, max_length=30)
    fecha_oferta_utc: datetime | None = Field(default=None)
    fecha_respuesta_utc: datetime | None = Field(default=None)


class ReubicacionResponse(ReubicacionBase):
    id_reubicacion: int
    model_config = ConfigDict(from_attributes=True)

