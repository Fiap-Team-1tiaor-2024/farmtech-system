from fastapi import FastAPI
from .routers import fase1, fase2, fase3, fase4, estatistica, farmtech

app = FastAPI()

# Inclui os roteadores
app.include_router(fase1.router, prefix="/v1/farmtech/fase1")
app.include_router(fase2.router, prefix="/v1/farmtech/fase2")
app.include_router(fase3.router, prefix="/v1/farmtech/fase3")
app.include_router(fase4.router, prefix="/v1/farmtech/fase4")
app.include_router(estatistica.router, prefix="/v1/farmtech/analise/r")
app.include_router(farmtech.router, prefix="/v1/farmtech")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)