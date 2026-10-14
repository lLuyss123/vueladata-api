from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ReservaBase(BaseModel):
    codigo_reserva: str = Field(..., max_length=20, min_length=1)
    fecha_reserva_utc: datetime = Field(...)
    estado_reserva: str = Field(..., max_length=30, min_length=1)
    fecha_actualizacion_utc: datetime = Field(...)


class ReservaCreate(ReservaBase):
    pass


class ReservaUpdate(BaseModel):
    codigo_reserva: str | None = Field(default=None, max_length=20, min_length=1)
    fecha_reserva_utc: datetime | None = Field(default=None)
    estado_reserva: str | None = Field(default=None, max_length=30, min_length=1)
    fecha_actualizacion_utc: datetime | None = Field(default=None)


class ReservaResponse(ReservaBase):
    id_reserva: int
    model_config = ConfigDict(from_attributes=True)

