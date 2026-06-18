from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:1234@host.docker.internal:5432/retaildb"
)

connection = engine.connect()

print("Database Connected Successfully!")