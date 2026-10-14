from pydantic import BaseModel, ConfigDict, Field


class ReservaPasajeroBase(BaseModel):
    id_reserva: int = Field(...)
    id_pasajero: int = Field(...)


class ReservaPasajeroCreate(ReservaPasajeroBase):
    pass


class ReservaPasajeroUpdate(BaseModel):
    id_reserva: int | None = Field(default=None)
    id_pasajero: int | None = Field(default=None)


class ReservaPasajeroResponse(ReservaPasajeroBase):
    id_reserva_pasajero: int
    model_config = ConfigDict(from_attributes=True)

