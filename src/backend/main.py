from fastapi import FastAPI
from routers import estatistica, farmtech
import uvicorn

app = FastAPI()

# Inclui os roteadores
app.include_router(estatistica.router, prefix="/v1/farmtech/analises/r")
app.include_router(farmtech.router, prefix="/v1/farmtech")
