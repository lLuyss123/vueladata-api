from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class AuditoriaCausaBase(BaseModel):
    id_incidencia: int = Field(...)
    id_observacion_clima_origen: int | None = Field(default=None)
    id_observacion_clima_destino: int | None = Field(default=None)
    motivo: str = Field(..., max_length=500, min_length=1)
    estado: Literal['PENDIENTE', 'CONFIRMADA', 'DESCARTADA'] = Field(..., max_length=30)
    fecha_creacion_utc: datetime = Field(...)
    fecha_resolucion_utc: datetime | None = Field(default=None)


class AuditoriaCausaCreate(AuditoriaCausaBase):
    pass


class AuditoriaCausaUpdate(BaseModel):
    id_incidencia: int | None = Field(default=None)
    id_observacion_clima_origen: int | None = Field(default=None)
    id_observacion_clima_destino: int | None = Field(default=None)
    motivo: str | None = Field(default=None, max_length=500, min_length=1)
    estado: Literal['PENDIENTE', 'CONFIRMADA', 'DESCARTADA'] | None = Field(default=None, max_length=30)
    fecha_creacion_utc: datetime | None = Field(default=None)
    fecha_resolucion_utc: datetime | None = Field(default=None)


class AuditoriaCausaResponse(AuditoriaCausaBase):
    id_auditoria: int
    model_config = ConfigDict(from_attributes=True)

