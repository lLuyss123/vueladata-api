from pydantic import BaseModel, ConfigDict, Field


class ConexionItinerarioBase(BaseModel):
    id_regla_conexion: int = Field(...)
    id_detalle_reserva_llegada: int = Field(...)
    id_detalle_reserva_salida: int = Field(...)


class ConexionItinerarioCreate(ConexionItinerarioBase):
    pass


class ConexionItinerarioUpdate(BaseModel):
    id_regla_conexion: int | None = Field(default=None)
    id_detalle_reserva_llegada: int | None = Field(default=None)
    id_detalle_reserva_salida: int | None = Field(default=None)


class ConexionItinerarioResponse(ConexionItinerarioBase):
    id_conexion: int
    model_config = ConfigDict(from_attributes=True)

