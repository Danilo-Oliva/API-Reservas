from fastapi import FastAPI
from src.database import engine, Base

from src.models.usuario import Usuario
from src.models.reserva import Reserva

from src.routers.usuarios import router as usuarios_routers

app = FastAPI(title="Sistema de Reservas API", version="1.0.0")

Base.metadata.create_all(bind=engine)
app.include_router(usuarios_routers)


@app.get("/")
def leer_raiz():
    return {"mensaje": "API de reservas funcionando correctamente"}
