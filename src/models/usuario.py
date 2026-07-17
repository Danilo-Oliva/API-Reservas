from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.database import Base


class Usuario(Base):
    # Pasar nombre de la tabla a SQLAlchemy
    __tablename__ = "usuarios"

    # definir las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)

    # unique para que no hayan 2 personas con el mismo mail
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(Integer, nullable=True)

    # guardar la fecha exata del registro de forma automatica
    fecha_registro = Column(DateTime, default=datetime.now(timezone.utc))

    # crear relacion virtual con el modelo Reserva
    #'back_populates' conecta el modelo Usuarios con el campo 'cliente' de la Reserva
    reservas = relationship(
        "Reserva", back_populates="cliente", cascade="all, delete-orphan"
    )
