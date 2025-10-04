from fastapi import FastAPI
from routes import posts,users,login,votes
from models import Base
from database import engine
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}
