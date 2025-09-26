from fastapi import FastAPI
from routes import posts,users,login

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(login.router)