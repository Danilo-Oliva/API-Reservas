from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional


# lo que el cliente envia para agendar el turno (request)
class ReservaCreate(BaseModel):
    usuario_id: int
    fecha_hora: datetime
    servicio: str


# lo que se le respone al cliente una vez creada (response)
class ReservaResponse(BaseModel):
    id: int
    usuario_id: int
    fecha_hora: datetime
    servicio: str
    estado: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True
