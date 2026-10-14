from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class ReglaRotacionBase(BaseModel):
    tipo_vuelo: Literal['NACIONAL', 'INTERNACIONAL'] = Field(..., max_length=20)
    minutos_minimos: int = Field(...)
    vigente_desde_utc: datetime = Field(...)
    vigente_hasta_utc: datetime | None = Field(default=None)


class ReglaRotacionCreate(ReglaRotacionBase):
    pass


class ReglaRotacionUpdate(BaseModel):
    tipo_vuelo: Literal['NACIONAL', 'INTERNACIONAL'] | None = Field(default=None, max_length=20)
    minutos_minimos: int | None = Field(default=None)
    vigente_desde_utc: datetime | None = Field(default=None)
    vigente_hasta_utc: datetime | None = Field(default=None)


class ReglaRotacionResponse(ReglaRotacionBase):
    id_regla_rotacion: int
    model_config = ConfigDict(from_attributes=True)

