
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,text
from database import Base

class POST(Base):
    __tablename__='posts'

    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    published=Column(Boolean,server_default='TRUE')
    created_at=Column(TIMESTAMP(timezone=True),server_default=text('now()'))
    
class USER(Base):
    __tablename__='users'

    id=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=text('now()'),nullable=False)

