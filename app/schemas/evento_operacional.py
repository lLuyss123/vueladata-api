from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class EventoOperacionalBase(BaseModel):
    id_vuelo: int = Field(...)
    id_estado_vuelo: int = Field(...)
    fecha_hora_evento_utc: datetime = Field(...)
    fecha_hora_recepcion_utc: datetime = Field(...)
    codigo_evento: str = Field(..., max_length=40, min_length=1)
    codigo_causa_original: str | None = Field(default=None, max_length=50)
    id_externo_evento: str = Field(..., max_length=150, min_length=1)
    estado_validacion: Literal['PENDIENTE', 'VALIDO', 'RECHAZADO'] = Field(..., max_length=20)
    detalle_validacion: str | None = Field(default=None, max_length=500)
    fecha_procesamiento_utc: datetime | None = Field(default=None)


class EventoOperacionalCreate(EventoOperacionalBase):
    pass


class EventoOperacionalUpdate(BaseModel):
    id_vuelo: int | None = Field(default=None)
    id_estado_vuelo: int | None = Field(default=None)
    fecha_hora_evento_utc: datetime | None = Field(default=None)
    fecha_hora_recepcion_utc: datetime | None = Field(default=None)
    codigo_evento: str | None = Field(default=None, max_length=40, min_length=1)
    codigo_causa_original: str | None = Field(default=None, max_length=50)
    id_externo_evento: str | None = Field(default=None, max_length=150, min_length=1)
    estado_validacion: Literal['PENDIENTE', 'VALIDO', 'RECHAZADO'] | None = Field(default=None, max_length=20)
    detalle_validacion: str | None = Field(default=None, max_length=500)
    fecha_procesamiento_utc: datetime | None = Field(default=None)


class EventoOperacionalResponse(EventoOperacionalBase):
    id_evento: int
    model_config = ConfigDict(from_attributes=True)

