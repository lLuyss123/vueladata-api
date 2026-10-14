from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class ProyeccionPropagacionBase(BaseModel):
    id_vuelo_origen: int = Field(...)
    id_vuelo_afectado: int = Field(...)
    id_regla_rotacion: int = Field(...)
    retraso_origen_min: int = Field(...)
    retraso_proyectado_min: int = Field(...)
    fecha_calculo_utc: datetime = Field(...)
    estado: Literal['PROYECTADA', 'CONFIRMADA', 'DESCARTADA'] = Field(..., max_length=30)


class ProyeccionPropagacionCreate(ProyeccionPropagacionBase):
    pass


class ProyeccionPropagacionUpdate(BaseModel):
    id_vuelo_origen: int | None = Field(default=None)
    id_vuelo_afectado: int | None = Field(default=None)
    id_regla_rotacion: int | None = Field(default=None)
    retraso_origen_min: int | None = Field(default=None)
    retraso_proyectado_min: int | None = Field(default=None)
    fecha_calculo_utc: datetime | None = Field(default=None)
    estado: Literal['PROYECTADA', 'CONFIRMADA', 'DESCARTADA'] | None = Field(default=None, max_length=30)


class ProyeccionPropagacionResponse(ProyeccionPropagacionBase):
    id_proyeccion: int
    model_config = ConfigDict(from_attributes=True)

