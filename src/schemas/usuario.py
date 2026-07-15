# srive para validacion y transformacion de datos en tiempo de ejecucion
from pydantic import BaseModel, EmailStr
from typing import Optional


# esquema que define que datos se requieren para crear un usuario nuevo (request)
class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    telefono: Optional[str] = None


# esquima que define que tipo de datos le devolvemos al cliente (response)
class UsuarioRespone(BaseModel):
    id: int
    nombre: str
    email: str
    
    #configuracion que permite a pydantic leer los modelos de sqlalchemy
    class Config:
        from_attributes = True