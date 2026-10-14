from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class VueloBase(BaseModel):
    id_ruta: int = Field(...)
    id_aeronave: int = Field(...)
    numero_vuelo: str = Field(..., max_length=12, min_length=1)
    salida_programada_utc: datetime = Field(...)
    llegada_programada_utc: datetime = Field(...)
    salida_real_puerta_utc: datetime | None = Field(default=None)
    despegue_real_utc: datetime | None = Field(default=None)
    aterrizaje_real_utc: datetime | None = Field(default=None)
    llegada_real_puerta_utc: datetime | None = Field(default=None)
    id_estado_vuelo_actual: int = Field(...)
    id_aeropuerto_desvio: int | None = Field(default=None)


class VueloCreate(VueloBase):
    pass


class VueloUpdate(BaseModel):
    id_ruta: int | None = Field(default=None)
    id_aeronave: int | None = Field(default=None)
    numero_vuelo: str | None = Field(default=None, max_length=12, min_length=1)
    salida_programada_utc: datetime | None = Field(default=None)
    llegada_programada_utc: datetime | None = Field(default=None)
    salida_real_puerta_utc: datetime | None = Field(default=None)
    despegue_real_utc: datetime | None = Field(default=None)
    aterrizaje_real_utc: datetime | None = Field(default=None)
    llegada_real_puerta_utc: datetime | None = Field(default=None)
    id_estado_vuelo_actual: int | None = Field(default=None)
    id_aeropuerto_desvio: int | None = Field(default=None)


class VueloResponse(VueloBase):
    id_vuelo: int
    model_config = ConfigDict(from_attributes=True)

