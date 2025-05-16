from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from infra.database.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CULTURA
@router.post("/cultura/", response_model=schemas.Cultura)
def create_cultura(cultura: schemas.CulturaCreate, db: Session = Depends(get_db)):
    db_cultura = models.Cultura(**cultura.dict())
    db.add(db_cultura)
    db.commit()
    db.refresh(db_cultura)
    return db_cultura

@router.get("/cultura/", response_model=list[schemas.Cultura])
def list_culturas(db: Session = Depends(get_db)):
    return db.query(models.Cultura).all()


# Similar para Propriedade, Producao e Insumo...
@router.post("/propriedade/", response_model=schemas.Propriedade)
def create_propriedade(propriedade: schemas.PropriedadeCreate, db: Session = Depends(get_db)):
    db_propriedade = models.Propriedade(**propriedade.dict())
    db.add(db_propriedade)
    db.commit()
    db.refresh(db_propriedade)
    return db_propriedade

@router.get("/propriedade/", response_model=list[schemas.Propriedade])
def list_propriedades(db: Session = Depends(get_db)):
    return db.query(models.Propriedade).all()

@router.post("/producao/", response_model=schemas.Producao)
def create_producao(producao: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    db_producao = models.Producao(**producao.dict())
    db.add(db_producao)
    db.commit()
    db.refresh(db_producao)
    return db_producao

@router.get("/producao/", response_model=list[schemas.Producao])
def list_producoes(db: Session = Depends(get_db)):
    return db.query(models.Producao).all()