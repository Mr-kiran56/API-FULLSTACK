from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database:str
    database_name:str
    password:str
    host:str
    secret_key:str
    algorithm:str
    expire_time:int
    class Config:
        env_file='.env'

settings=Settings()
