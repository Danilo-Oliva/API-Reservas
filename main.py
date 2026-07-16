from fastapi import FastAPI
from src.database import engine, Base

from src.models.usuario import Usuario
from src.models.reserva import Reserva

from src.routers.usuarios import router as usuarios_router
from src.routers.reservas import router as reservas_router

app = FastAPI(title="Sistema de Reservas API", version="1.0.0")

# crear tablas
Base.metadata.create_all(bind=engine)

# incluir routers
app.include_router(usuarios_router)
app.include_router(reservas_router)


@app.get("/")
def leer_raiz():
    return {"mensaje": "API de reservas funcionando correctamente"}
