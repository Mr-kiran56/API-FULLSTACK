from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

password = quote_plus("KIRAN5656@")

SQL_DATABASE_URL = f"postgresql://postgres:{password}@localhost/FastAPI"

engine = create_engine(SQL_DATABASE_URL, connect_args={"options": "-c timezone=utc"})

SessionMaker = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()
