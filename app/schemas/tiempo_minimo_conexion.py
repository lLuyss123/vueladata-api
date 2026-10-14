from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class TiempoMinimoConexionBase(BaseModel):
    id_aeropuerto: int = Field(...)
    tipo_llegada: Literal['NACIONAL', 'INTERNACIONAL'] = Field(..., max_length=20)
    tipo_salida: Literal['NACIONAL', 'INTERNACIONAL'] = Field(..., max_length=20)
    minutos_minimos: int = Field(...)
    vigente_desde_utc: datetime = Field(...)
    vigente_hasta_utc: datetime | None = Field(default=None)


class TiempoMinimoConexionCreate(TiempoMinimoConexionBase):
    pass


class TiempoMinimoConexionUpdate(BaseModel):
    id_aeropuerto: int | None = Field(default=None)
    tipo_llegada: Literal['NACIONAL', 'INTERNACIONAL'] | None = Field(default=None, max_length=20)
    tipo_salida: Literal['NACIONAL', 'INTERNACIONAL'] | None = Field(default=None, max_length=20)
    minutos_minimos: int | None = Field(default=None)
    vigente_desde_utc: datetime | None = Field(default=None)
    vigente_hasta_utc: datetime | None = Field(default=None)


class TiempoMinimoConexionResponse(TiempoMinimoConexionBase):
    id_regla_conexion: int
    model_config = ConfigDict(from_attributes=True)

