from datetime import datetime, timezone
from src.database import SessionLocal
from src.models.usuario import Usuario
from src.models.reserva import Reserva

def probar_base_de_datos():
  # 1 - crear   una sesion para interactuar con la base de datos
  db = SessionLocal()
  
  try:
    print('\n---1. Creando usuario de prueba ---')
    # instanciar la clase usuario
    nuevo_usuario = Usuario(
      nombre = "Dani",
      email = "dani@correo.com",
      telefono = "12345678"
    )
    
    # decir a la sesion que queremos guardar el usuario
    db.add(nuevo_usuario)
    # hacer el commit
    db.commit()
    # refrescar el objeto para que Python sepa que id le asigno la DB
    db.refresh(nuevo_usuario)
    
    print(f'Usuario creado. ID: {nuevo_usuario.id}, Nombre: {nuevo_usuario.nombre}')
    
    print(f'\n--- 2. Creando una reserva asociada al usuario {nuevo_usuario.id}')
    
    #crear una reserva
    fecha_reserva = datetime(2026, 7, 15, 18, 0, 0)
    
    nueva_reserva = Reserva(
      usuario_id = nuevo_usuario.id,
      fecha_hora = fecha_reserva,
      servicio = "Clases de Funcional",
      estado = "confirmada"
    )
    
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)
    
    print(f"Reserva creada. ID: {nueva_reserva.id} para el servicio '{nueva_reserva.servicio}'")
  except Exception as e:
    # En caso de fallar, deshacer los cambios para evitar datos corruptos
    db.rollback()
    print(f"Ocurrió un error inesperado {e}")
  finally:
    # al final se cierra la sesion para liberar la DB
    db.close()
    print('\nConexión con la base de datos cerrada de manera segura.')

if __name__ == '__main__':
  probar_base_de_datos()