from src.database import engine, Base
from src.models.usuario import Usuario
from src.models.reserva import Reserva

def inicializar_base_de_datos():
  # crear fisicamente el archivo reservas.db y sus tablas
  Base.metadata.create_all(bind=engine)
  print("Base de datos y tabla creadas exitosamente")
  
if __name__ == "__main__":
  inicializar_base_de_datos()