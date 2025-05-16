from fastapi import FastAPI
from routers import estatistica, farmtech

app = FastAPI()

# Inclui os roteadores
app.include_router(estatistica.router, prefix="/v1/farmtech/analise/r")
app.include_router(farmtech.router, prefix="/v1/farmtech")