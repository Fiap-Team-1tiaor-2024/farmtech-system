from database.database import Base, engine

print("Criando tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")