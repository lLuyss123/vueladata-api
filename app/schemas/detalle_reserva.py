from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class DetalleReservaBase(BaseModel):
    id_itinerario: int = Field(...)
    id_vuelo: int = Field(...)
    numero_secuencia: int = Field(...)
    clase_servicio: str = Field(..., max_length=40, min_length=1)
    clase_tarifaria: str | None = Field(default=None, max_length=20)
    monto_tarifa_pagada: Decimal = Field(...)
    moneda: str = Field(..., max_length=3, min_length=1)
    numero_asiento: str | None = Field(default=None, max_length=10)
    estado_segmento: str = Field(..., max_length=30, min_length=1)


class DetalleReservaCreate(DetalleReservaBase):
    pass


class DetalleReservaUpdate(BaseModel):
    id_itinerario: int | None = Field(default=None)
    id_vuelo: int | None = Field(default=None)
    numero_secuencia: int | None = Field(default=None)
    clase_servicio: str | None = Field(default=None, max_length=40, min_length=1)
    clase_tarifaria: str | None = Field(default=None, max_length=20)
    monto_tarifa_pagada: Decimal | None = Field(default=None)
    moneda: str | None = Field(default=None, max_length=3, min_length=1)
    numero_asiento: str | None = Field(default=None, max_length=10)
    estado_segmento: str | None = Field(default=None, max_length=30, min_length=1)


class DetalleReservaResponse(DetalleReservaBase):
    id_detalle_reserva: int
    model_config = ConfigDict(from_attributes=True)

