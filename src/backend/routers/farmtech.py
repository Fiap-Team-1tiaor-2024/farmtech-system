from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from infra.database.database import SessionLocal
from infra.database.database import *

router = APIRouter()

@router.post("/cultura", response_model=schemas.Cultura, status_code=status.HTTP_201_CREATED)
def criar_cultura(cultura: schemas.CulturaCreate, db: Session = Depends(get_db)):
    db_cultura = models.Cultura(**cultura.dict())
    db.add(db_cultura)
    db.commit()
    db.refresh(db_cultura)
    return db_cultura

@router.get("/cultura", response_model=list[schemas.Cultura], status_code=status.HTTP_200_OK)
def listar_cultura(db: Session = Depends(get_db)):
    return db.query(models.Cultura).all()

@router.post("/propriedade", response_model=schemas.Propriedade, status_code=status.HTTP_201_CREATED)
def criar_propriedade(propriedade: schemas.PropriedadeCreate, db: Session = Depends(get_db)):
    db_propriedade = models.Propriedade(**propriedade.dict())
    db.add(db_propriedade)
    db.commit()
    db.refresh(db_propriedade)
    return db_propriedade

@router.get("/propriedade", response_model=list[schemas.Propriedade], status_code=status.HTTP_200_OK)
def listar_propriedades(db: Session = Depends(get_db)):
    return db.query(models.Propriedade).all()

@router.post("/producao", response_model=schemas.Producao, status_code=status.HTTP_201_CREATED)
def criar_producao(producao: schemas.ProducaoCreate, db: Session = Depends(get_db)):
    db_producao = models.Producao(**producao.dict())
    db.add(db_producao)
    db.commit()
    db.refresh(db_producao)
    return db_producao

@router.get("/producao", response_model=list[schemas.Producao], status_code=status.HTTP_200_OK)
def listar_producoes(db: Session = Depends(get_db)):
    return db.query(models.Producao).all()