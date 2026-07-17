from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.database import Base


class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # clave foranea que conecta la columna con el 'id de la tabla 'usuarios'
    usuario_id = Column(
        Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False
    )

    fecha_hora = Column(DateTime, nullable=False)
    servicio = Column(String, nullable=False)
    estado = Column(String, default="confirmada")
    fecha_creacion = Column(DateTime, default=datetime.now(timezone.utc))

    # relacion inversa. permite hacer mi_reserva.cliente.nombre
    cliente = relationship("Usuario", back_populates="reservas")
