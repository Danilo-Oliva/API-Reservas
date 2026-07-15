from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate, UsuarioResponse

# crear el router para modularizar las rutas de usuarios
router = APIRouter(
  # agrega el prefijo /usuarios a todos los endpoints de este archivo
  prefix="/usuarios",
  #los agrupa bajo la seccion usuarios en la documentacion
  tags=["Usuarios"]
)

#dependencia locar para la sesion de bd
def get_db():
  db = SessionLocal()
  try:
    # mantiene congelada la funcion hasta que la app termine de usar la db
    yield db
  finally:
    db.close()
    
# ruta para crear un usuario
@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
  usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
  
  if usuario_existente:
    raise HTTPException(status_code=400, detail="El email ya está registrado.")
  
  nuevo_usuario = Usuario(
    nombre= usuario.nombre,
    email= usuario.email,
    telefono= usuario.telefono
  )
  
  db.add(nuevo_usuario)
  db.commit()
  db.refresh(nuevo_usuario)
  
  return nuevo_usuario