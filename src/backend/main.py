from fastapi import FastAPI
from routers import fase1, fase2, fase3, fase4, estatistica

app = FastAPI()

# Inclui os roteadores
app.include_router(fase1.router, prefix="/v1/fase1")
app.include_router(fase2.router, prefix="/v1/fase2")
app.include_router(fase3.router, prefix="/v1/fase3")
app.include_router(fase4.router, prefix="/v1/fase4")
app.include_router(fase4.router, prefix="/v1/analise/r")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)