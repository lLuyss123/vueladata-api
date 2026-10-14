from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class NotificacionBase(BaseModel):
    id_detalle_reserva: int = Field(...)
    id_evaluacion_conexion: int | None = Field(default=None)
    id_compensacion: int | None = Field(default=None)
    tipo: Literal['CONEXION_RIESGO', 'COMPENSACION', 'REUBICACION', 'INTERRUPCION'] = Field(..., max_length=30)
    canal: Literal['EMAIL', 'SMS', 'PUSH'] = Field(..., max_length=20)
    estado_envio: Literal['PENDIENTE', 'ENVIADA', 'FALLIDA'] = Field(..., max_length=30)
    fecha_programada_utc: datetime = Field(...)
    fecha_envio_utc: datetime | None = Field(default=None)


class NotificacionCreate(NotificacionBase):
    pass


class NotificacionUpdate(BaseModel):
    id_detalle_reserva: int | None = Field(default=None)
    id_evaluacion_conexion: int | None = Field(default=None)
    id_compensacion: int | None = Field(default=None)
    tipo: Literal['CONEXION_RIESGO', 'COMPENSACION', 'REUBICACION', 'INTERRUPCION'] | None = Field(default=None, max_length=30)
    canal: Literal['EMAIL', 'SMS', 'PUSH'] | None = Field(default=None, max_length=20)
    estado_envio: Literal['PENDIENTE', 'ENVIADA', 'FALLIDA'] | None = Field(default=None, max_length=30)
    fecha_programada_utc: datetime | None = Field(default=None)
    fecha_envio_utc: datetime | None = Field(default=None)


class NotificacionResponse(NotificacionBase):
    id_notificacion: int
    model_config = ConfigDict(from_attributes=True)

