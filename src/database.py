""" Conexion a la DB y sesión de SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1- Definir la url de la DB
# "sqlite:///" sirve para indicar que es un DB locar en el archivo llamado "./nombre_Del_archivo.db"
DATABASE_URL = "sqlite:///./reservas.db"

# 2 - Crear el Engine(motor), es el puente real entre Python y SQL
# 'connect_args' solo se necesita en  SQLite para permitir que multiples hilos interactuen con el
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#3  Crear la fabrica de sesiones(SessionLocal)
# cada vez que un usuario haga una reserva, se abre una sesion de esta fabrica para operar
  # =====================================================================
  # AUTOCOMMIT -> evita que se guarden los cambios automaticamente tras cada operacion, obliga a usar session.commit()
  # AUTOFLUSH -> evita que se notifique de cambios pendientes a la DB ciuando hacemos un cambio
  # BIND -> Le indica a que DB debe conectarse
  # =====================================================================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 