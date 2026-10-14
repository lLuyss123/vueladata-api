from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class PosicionAeronaveBase(BaseModel):
    id_aeronave: int = Field(...)
    fecha_hora_posicion_utc: datetime = Field(...)
    fecha_hora_recepcion_utc: datetime = Field(...)
    latitud: Decimal = Field(...)
    longitud: Decimal = Field(...)
    altitud_m: Decimal | None = Field(default=None)
    velocidad_kmh: Decimal | None = Field(default=None)
    rumbo_grados: Decimal | None = Field(default=None)
    en_tierra: bool = Field(...)
    id_externo_posicion: str = Field(..., max_length=150, min_length=1)


class PosicionAeronaveCreate(PosicionAeronaveBase):
    pass


class PosicionAeronaveUpdate(BaseModel):
    id_aeronave: int | None = Field(default=None)
    fecha_hora_posicion_utc: datetime | None = Field(default=None)
    fecha_hora_recepcion_utc: datetime | None = Field(default=None)
    latitud: Decimal | None = Field(default=None)
    longitud: Decimal | None = Field(default=None)
    altitud_m: Decimal | None = Field(default=None)
    velocidad_kmh: Decimal | None = Field(default=None)
    rumbo_grados: Decimal | None = Field(default=None)
    en_tierra: bool | None = Field(default=None)
    id_externo_posicion: str | None = Field(default=None, max_length=150, min_length=1)


class PosicionAeronaveResponse(PosicionAeronaveBase):
    id_posicion: int
    model_config = ConfigDict(from_attributes=True)

