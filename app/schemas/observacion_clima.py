from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class ObservacionClimaBase(BaseModel):
    id_aeropuerto: int = Field(...)
    fecha_hora_observacion_utc: datetime = Field(...)
    fecha_hora_recepcion_utc: datetime = Field(...)
    visibilidad_km: Decimal | None = Field(default=None)
    velocidad_viento_kmh: Decimal | None = Field(default=None)
    direccion_viento_grados: Decimal | None = Field(default=None)
    temperatura_c: Decimal | None = Field(default=None)
    precipitacion_mm: Decimal | None = Field(default=None)
    codigo_clima: str | None = Field(default=None, max_length=30)


class ObservacionClimaCreate(ObservacionClimaBase):
    pass


class ObservacionClimaUpdate(BaseModel):
    id_aeropuerto: int | None = Field(default=None)
    fecha_hora_observacion_utc: datetime | None = Field(default=None)
    fecha_hora_recepcion_utc: datetime | None = Field(default=None)
    visibilidad_km: Decimal | None = Field(default=None)
    velocidad_viento_kmh: Decimal | None = Field(default=None)
    direccion_viento_grados: Decimal | None = Field(default=None)
    temperatura_c: Decimal | None = Field(default=None)
    precipitacion_mm: Decimal | None = Field(default=None)
    codigo_clima: str | None = Field(default=None, max_length=30)


class ObservacionClimaResponse(ObservacionClimaBase):
    id_observacion_clima: int
    model_config = ConfigDict(from_attributes=True)

