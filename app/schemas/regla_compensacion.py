from datetime import datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class ReglaCompensacionBase(BaseModel):
    tipo_incidencia: Literal['RETRASO', 'CANCELACION'] = Field(..., max_length=20)
    minutos_minimos: int | None = Field(default=None)
    minutos_maximos: int | None = Field(default=None)
    aviso_max_horas: int | None = Field(default=None)
    porcentaje: Decimal = Field(...)
    requiere_reubicacion: bool = Field(...)
    vigente_desde_utc: datetime = Field(...)
    vigente_hasta_utc: datetime | None = Field(default=None)


class ReglaCompensacionCreate(ReglaCompensacionBase):
    pass


class ReglaCompensacionUpdate(BaseModel):
    tipo_incidencia: Literal['RETRASO', 'CANCELACION'] | None = Field(default=None, max_length=20)
    minutos_minimos: int | None = Field(default=None)
    minutos_maximos: int | None = Field(default=None)
    aviso_max_horas: int | None = Field(default=None)
    porcentaje: Decimal | None = Field(default=None)
    requiere_reubicacion: bool | None = Field(default=None)
    vigente_desde_utc: datetime | None = Field(default=None)
    vigente_hasta_utc: datetime | None = Field(default=None)


class ReglaCompensacionResponse(ReglaCompensacionBase):
    id_regla_compensacion: int
    model_config = ConfigDict(from_attributes=True)

