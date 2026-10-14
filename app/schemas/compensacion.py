from datetime import datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class CompensacionBase(BaseModel):
    id_detalle_reserva: int = Field(...)
    id_incidencia: int = Field(...)
    id_regla_compensacion: int = Field(...)
    minutos_imputables: int | None = Field(default=None)
    monto: Decimal = Field(...)
    moneda: str = Field(..., max_length=3, min_length=1)
    fecha_calculo_utc: datetime = Field(...)
    estado: Literal['CALCULADA', 'SOLICITADA', 'PAGADA', 'RECHAZADA', 'ANULADA'] = Field(..., max_length=30)


class CompensacionCreate(CompensacionBase):
    pass


class CompensacionUpdate(BaseModel):
    id_detalle_reserva: int | None = Field(default=None)
    id_incidencia: int | None = Field(default=None)
    id_regla_compensacion: int | None = Field(default=None)
    minutos_imputables: int | None = Field(default=None)
    monto: Decimal | None = Field(default=None)
    moneda: str | None = Field(default=None, max_length=3, min_length=1)
    fecha_calculo_utc: datetime | None = Field(default=None)
    estado: Literal['CALCULADA', 'SOLICITADA', 'PAGADA', 'RECHAZADA', 'ANULADA'] | None = Field(default=None, max_length=30)


class CompensacionResponse(CompensacionBase):
    id_compensacion: int
    model_config = ConfigDict(from_attributes=True)

