from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class IncidenciaVueloBase(BaseModel):
    id_vuelo: int = Field(...)
    id_evento_origen: int = Field(...)
    id_causa: int = Field(...)
    tipo: Literal['RETRASO', 'CANCELACION'] = Field(..., max_length=20)
    minutos_retraso: int | None = Field(default=None)
    es_causa_principal: bool = Field(...)
    requiere_auditoria: bool = Field(...)
    estado_revision: Literal['PENDIENTE', 'APROBADA', 'RECHAZADA'] = Field(..., max_length=30)
    fecha_clasificacion_utc: datetime = Field(...)


class IncidenciaVueloCreate(IncidenciaVueloBase):
    pass


class IncidenciaVueloUpdate(BaseModel):
    id_vuelo: int | None = Field(default=None)
    id_evento_origen: int | None = Field(default=None)
    id_causa: int | None = Field(default=None)
    tipo: Literal['RETRASO', 'CANCELACION'] | None = Field(default=None, max_length=20)
    minutos_retraso: int | None = Field(default=None)
    es_causa_principal: bool | None = Field(default=None)
    requiere_auditoria: bool | None = Field(default=None)
    estado_revision: Literal['PENDIENTE', 'APROBADA', 'RECHAZADA'] | None = Field(default=None, max_length=30)
    fecha_clasificacion_utc: datetime | None = Field(default=None)


class IncidenciaVueloResponse(IncidenciaVueloBase):
    id_incidencia: int
    model_config = ConfigDict(from_attributes=True)

