from pydantic import BaseModel,EmailStr
from sqlalchemy import TIMESTAMP
from datetime import datetime
from typing import Optional
class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool] = True 

class User(BaseModel):
    email:EmailStr
    password:str

class Show_User(BaseModel):
    email:str
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None