from infra.database.database import Base, engine
from backend.models.models import Cultura, Propriedade, Producao, Insumo

print("Criando tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")