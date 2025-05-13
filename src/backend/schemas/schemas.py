from pydantic import BaseModel
from typing import Optional, List

# Cultura
class CulturaBase(BaseModel):
    nome: str

class CulturaCreate(CulturaBase):
    pass

class Cultura(CulturaBase):
    id: int
    class Config:
        orm_mode = True


# Propriedade
class PropriedadeBase(BaseModel):
    nome: str
    localizacao: Optional[str]

class PropriedadeCreate(PropriedadeBase):
    pass

class Propriedade(PropriedadeBase):
    id: int
    class Config:
        orm_mode = True


# Producao
class ProducaoBase(BaseModel):
    id_cultura: int
    id_propriedade: int
    area: float
    custo_producao: float

class ProducaoCreate(ProducaoBase):
    pass

class Producao(ProducaoBase):
    id: int
    class Config:
        orm_mode = True


# Insumo
class InsumoBase(BaseModel):
    tipo: str
    nome: str
    quantidade: float
    id_producao: int

class InsumoCreate(InsumoBase):
    pass

class Insumo(InsumoBase):
    id: int
    class Config:
        orm_mode = True
