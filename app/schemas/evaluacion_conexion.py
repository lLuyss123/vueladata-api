from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class EvaluacionConexionBase(BaseModel):
    id_conexion: int = Field(...)
    fecha_evaluacion_utc: datetime = Field(...)
    llegada_estimada_utc: datetime = Field(...)
    salida_estimada_utc: datetime = Field(...)
    minutos_disponibles: int = Field(...)
    minutos_requeridos: int = Field(...)
    estado: Literal['NORMAL', 'EN_RIESGO', 'PERDIDA'] = Field(..., max_length=20)


class EvaluacionConexionCreate(EvaluacionConexionBase):
    pass


class EvaluacionConexionUpdate(BaseModel):
    id_conexion: int | None = Field(default=None)
    fecha_evaluacion_utc: datetime | None = Field(default=None)
    llegada_estimada_utc: datetime | None = Field(default=None)
    salida_estimada_utc: datetime | None = Field(default=None)
    minutos_disponibles: int | None = Field(default=None)
    minutos_requeridos: int | None = Field(default=None)
    estado: Literal['NORMAL', 'EN_RIESGO', 'PERDIDA'] | None = Field(default=None, max_length=20)


class EvaluacionConexionResponse(EvaluacionConexionBase):
    id_evaluacion: int
    model_config = ConfigDict(from_attributes=True)

