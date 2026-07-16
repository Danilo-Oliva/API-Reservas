from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from src.database import SessionLocal
from src.models.reserva import Reserva
from src.models.usuario import Usuario
from src.schemas.reserva import ReservaCreate, ReservaResponse

router = APIRouter(
  prefix="/reservas",
  tags=["Reservas"]
)

# dependencia para la DB
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
    
@router.post("/", response_model=ReservaResponse)
def crear_reserva(reserva: ReservaCreate, db:Session = Depends(get_db)):
  # validar que el usuario exista
  usuario = db.query(Usuario).filter(Usuario.id == reserva.usuario_id).first()
  if not usuario:
    raise HTTPException(
      status_code=404,
      detail=f"No se puede crear la reserva. El usuario con ID{reserva.usuario_id} no existe."
    )
    
  # validar que la fecha no sea en el pasado
  ahora_utc = datetime.now(timezone.utc)
  
  if reserva.fecha_hora < ahora_utc:
    raise HTTPException(
      status_code=404,
      detail="No podés agendar una reserva para una fecha u hora que ya pasó."
    )
  
  # si pasó las validaciones, se crea la reserva
  nueva_reserva = Reserva(
    usuario_id = reserva.usuario_id,
    fecha_hora = reserva.fecha_hora,
    servicio = reserva.servicio
  )
  
  db.add(nueva_reserva)
  db.commit()
  db.refresh(nueva_reserva)
  
  return nueva_reserva