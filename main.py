from fastapi import FastAPI
from routes import posts,users,login,votes
from models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(votes.router)