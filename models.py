from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,TIMESTAMP,text
from database import Base

class POST(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("USER")  
    
class USER(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

    posts = relationship("POST", back_populates="owner") 