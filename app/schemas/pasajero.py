from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class PasajeroBase(BaseModel):
    nombre: str = Field(..., max_length=100, min_length=1)
    apellido: str = Field(..., max_length=100, min_length=1)
    documento: str = Field(..., max_length=50, min_length=1)
    tipo_documento: str = Field(..., max_length=30, min_length=1)
    fecha_nacimiento: date = Field(...)
    correo: str | None = Field(default=None, max_length=254)
    telefono: str | None = Field(default=None, max_length=30)


class PasajeroCreate(PasajeroBase):
    pass


class PasajeroUpdate(BaseModel):
    nombre: str | None = Field(default=None, max_length=100, min_length=1)
    apellido: str | None = Field(default=None, max_length=100, min_length=1)
    documento: str | None = Field(default=None, max_length=50, min_length=1)
    tipo_documento: str | None = Field(default=None, max_length=30, min_length=1)
    fecha_nacimiento: date | None = Field(default=None)
    correo: str | None = Field(default=None, max_length=254)
    telefono: str | None = Field(default=None, max_length=30)


class PasajeroResponse(PasajeroBase):
    id_pasajero: int
    model_config = ConfigDict(from_attributes=True)

