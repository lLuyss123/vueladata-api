from pydantic import BaseModel, ConfigDict, Field


class RutaBase(BaseModel):
    id_aeropuerto_origen: int = Field(...)
    id_aeropuerto_destino: int = Field(...)
    duracion_estimada_min: int = Field(...)


class RutaCreate(RutaBase):
    pass


class RutaUpdate(BaseModel):
    id_aeropuerto_origen: int | None = Field(default=None)
    id_aeropuerto_destino: int | None = Field(default=None)
    duracion_estimada_min: int | None = Field(default=None)


class RutaResponse(RutaBase):
    id_ruta: int
    model_config = ConfigDict(from_attributes=True)

