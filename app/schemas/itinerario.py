from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ItinerarioBase(BaseModel):
    id_reserva_pasajero: int = Field(...)
    fecha_salida_utc: datetime = Field(...)
    estado: str = Field(..., max_length=30, min_length=1)
    fecha_creacion_utc: datetime = Field(...)
    fecha_actualizacion_utc: datetime = Field(...)


class ItinerarioCreate(ItinerarioBase):
    pass


class ItinerarioUpdate(BaseModel):
    id_reserva_pasajero: int | None = Field(default=None)
    fecha_salida_utc: datetime | None = Field(default=None)
    estado: str | None = Field(default=None, max_length=30, min_length=1)
    fecha_creacion_utc: datetime | None = Field(default=None)
    fecha_actualizacion_utc: datetime | None = Field(default=None)


class ItinerarioResponse(ItinerarioBase):
    id_itinerario: int
    model_config = ConfigDict(from_attributes=True)

