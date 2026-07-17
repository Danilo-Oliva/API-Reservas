from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from src.database import SessionLocal
from src.models.reserva import Reserva
from src.models.usuario import Usuario
from src.schemas.reserva import ReservaCreate, ReservaResponse

router = APIRouter(prefix="/reservas", tags=["Reservas"])


# dependencia para la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ReservaResponse)
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    # validar que el usuario exista
    usuario = db.query(Usuario).filter(Usuario.id == reserva.usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail=f"No se puede crear la reserva. El usuario con ID{reserva.usuario_id} no existe.",
        )

    # validar que la fecha no sea en el pasado
    ahora_utc = datetime.now(timezone.utc)

    if reserva.fecha_hora < ahora_utc:
        raise HTTPException(
            status_code=404,
            detail="No podés agendar una reserva para una fecha u hora que ya pasó.",
        )

    # validar que no haya solapamiento para el mismo usuario
    # buscar si ya existe reserva del mismo usuario en ese mismo minuto exacto
    reserva_conflictiva = (
        db.query(Reserva)
        .filter(
            Reserva.usuario_id == reserva.usuario_id,
            Reserva.fecha_hora == reserva.fecha_hora,
            Reserva.estado == "confirmada",
        )
        .first()
    )

    if reserva_conflictiva:
        raise HTTPException(
            status_code=400,
            detail=f"Ya tenés una reserva activa para el servicio '{reserva_conflictiva.servicio}' en esa misma fecha y hora.",
        )

    # validar solapamiento del servicio
    # buscar si el servicio ya esta ocupado por otra persona a esa hora
    servicio_ocupado = (
        db.query(Reserva)
        .filter(
            Reserva.servicio == reserva.servicio,
            Reserva.fecha_hora == reserva.fecha_hora,
            Reserva.estado == "confirmada",
        )
        .first()
    )

    if servicio_ocupado:
        raise HTTPException(
            status_code=400,
            detail="Este horario ya está reservado para ese servicio por otro usuario.",
        )

    # si pasó las validaciones, se crea la reserva
    nueva_reserva = Reserva(
        usuario_id=reserva.usuario_id,
        fecha_hora=reserva.fecha_hora,
        servicio=reserva.servicio,
    )

    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)

    return nueva_reserva


# Endpoint para obtener todas las reservas registradas
@router.get("/", response_model=list[ReservaResponse])
def listar_todas_las_reservas(db: Session = Depends(get_db)):
    reservas = db.query(Reserva).all()
    return reservas


# endpoint para obtener todas las reservas de un mismo usuario en especifico
@router.get("/usuario/{usuario_id}", response_model=list[ReservaResponse])
def listar_reservas_de_usuario(usuario_id: int, db: Session = Depends(get_db)):
    # verificar que el usuario exista
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    # si no existe
    if not usuario:
        raise HTTPException(
            status_code=404, detail=f"El usuario con ID {usuario_id} no existe."
        )

    # si existe
    reservas_usuario = db.query(Reserva).filter(Reserva.usuario_id == usuario_id).all()

    return reservas_usuario
