from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Olá da fase 1!"}
