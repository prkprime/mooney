from decouple import config
from sqlmodel import SQLModel, create_engine

database_url = config("database_url")

engine = create_engine(database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
