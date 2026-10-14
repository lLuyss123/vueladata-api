from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class CheckinBase(BaseModel):
    id_detalle_reserva: int = Field(...)
    fecha_hora_checkin_utc: datetime = Field(...)
    estado_checkin: str = Field(..., max_length=30, min_length=1)
    numero_tarjeta_embarque: str | None = Field(default=None, max_length=60)
    equipaje_cantidad: int = Field(...)
    equipaje_peso: Decimal = Field(...)


class CheckinCreate(CheckinBase):
    pass


class CheckinUpdate(BaseModel):
    id_detalle_reserva: int | None = Field(default=None)
    fecha_hora_checkin_utc: datetime | None = Field(default=None)
    estado_checkin: str | None = Field(default=None, max_length=30, min_length=1)
    numero_tarjeta_embarque: str | None = Field(default=None, max_length=60)
    equipaje_cantidad: int | None = Field(default=None)
    equipaje_peso: Decimal | None = Field(default=None)


class CheckinResponse(CheckinBase):
    id_checkin: int
    model_config = ConfigDict(from_attributes=True)

