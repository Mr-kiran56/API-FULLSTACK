from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database:str
    database_name:str
    password:str
    host:str
    secret_key:str
    algorithm:str
    expire_time:int
    database_port:int
    db_name:str
    class Config:
        env_file='.env'

settings=Settings()
