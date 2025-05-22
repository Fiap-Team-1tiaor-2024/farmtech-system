from backend.models.models import Cultura, Insumo, Producao, Propriedade
from infra.database.database import Base, engine

print('Criando tabelas no banco...')
Base.metadata.create_all(bind=engine)
print('Tabelas criadas com sucesso!')
