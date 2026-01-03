from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool] = True 

class User(BaseModel):
    email: EmailStr
    password: str

class Show_User(BaseModel):
    id: int
    email: str
    created_at: datetime
    class Config:
        orm_mode = True


class Post(Blog):
    id: int
    owner: Show_User

    class Config:
        orm_mode = True

class Vote_Posts(BaseModel):
    Posts:Post
    votes:int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  
