from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus
from Config import settings

password = quote_plus(settings.password)

SQL_DATABASE_URL = f"{settings.database}://{settings.database_name}:{password}@{settings.host}/FastAPI"

engine = create_engine(SQL_DATABASE_URL, connect_args={"options": "-c timezone=utc"})

SessionMaker = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()
