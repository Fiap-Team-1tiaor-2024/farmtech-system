from fastapi import FastAPI
from routers import estatistica, farmtech, predicao

app = FastAPI()

# Inclui os roteadores
app.include_router(estatistica.router, prefix="/v1/farmtech/analises/r")
app.include_router(farmtech.router, prefix="/v1/farmtech")
app.include_router(predicao.router, prefix="/v1/farmtech")
