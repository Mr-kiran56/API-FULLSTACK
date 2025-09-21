from pydantic import BaseModel,EmailStr
from sqlalchemy import TIMESTAMP
from datetime import datetime
class Blog(BaseModel):
    title: str
    description: str
    published: bool 

class User(BaseModel):
    email:EmailStr
    password:str



class Show_User(BaseModel):
    email:str
    created_at: datetime
    class Config:
        from_attributes = True