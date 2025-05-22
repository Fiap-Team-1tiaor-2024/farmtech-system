from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from infra.database.database import Base

# Esse arquivo contém os modelos de dados para o SQLAlchemy.
# Os modelos são usados para mapear as tabelas do banco de dados e definir os relacionamentos entre elas.


class Cultura(Base):
    __tablename__ = 'cultura'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)

    producoes = relationship('Producao', back_populates='cultura')


class Propriedade(Base):
    __tablename__ = 'propriedade'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    localizacao = Column(String(255), nullable=True)

    producoes = relationship('Producao', back_populates='propriedade')


class Producao(Base):
    __tablename__ = 'producao'

    id = Column(Integer, primary_key=True, index=True)
    id_cultura = Column(Integer, ForeignKey('cultura.id'))
    id_propriedade = Column(Integer, ForeignKey('propriedade.id'))
    area = Column(Float)
    custo_producao = Column(Float)

    cultura = relationship('Cultura', back_populates='producoes')
    propriedade = relationship('Propriedade', back_populates='producoes')
    insumos = relationship('Insumo', back_populates='producao')


class Insumo(Base):
    __tablename__ = 'insumo'

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(255))
    nome = Column(String(255))
    quantidade = Column(Float)
    id_producao = Column(Integer, ForeignKey('producao.id'))

    producao = relationship('Producao', back_populates='insumos')
