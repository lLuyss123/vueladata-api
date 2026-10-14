from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class AeropuertoBase(BaseModel):
    id_ciudad: int = Field(...)
    codigo_iata: str = Field(..., max_length=3, min_length=1)
    codigo_icao: str | None = Field(default=None, max_length=4)
    nombre: str = Field(..., max_length=180, min_length=1)
    latitud: Decimal = Field(...)
    longitud: Decimal = Field(...)
    zona_horaria: str = Field(..., max_length=64, min_length=1)
    es_hub: bool = Field(...)


class AeropuertoCreate(AeropuertoBase):
    pass


class AeropuertoUpdate(BaseModel):
    id_ciudad: int | None = Field(default=None)
    codigo_iata: str | None = Field(default=None, max_length=3, min_length=1)
    codigo_icao: str | None = Field(default=None, max_length=4)
    nombre: str | None = Field(default=None, max_length=180, min_length=1)
    latitud: Decimal | None = Field(default=None)
    longitud: Decimal | None = Field(default=None)
    zona_horaria: str | None = Field(default=None, max_length=64, min_length=1)
    es_hub: bool | None = Field(default=None)


class AeropuertoResponse(AeropuertoBase):
    id_aeropuerto: int
    model_config = ConfigDict(from_attributes=True)

