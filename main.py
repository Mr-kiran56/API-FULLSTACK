from fastapi import FastAPI, status, HTTPException,Depends
# import psycopg2
# from psycopg2.extras import RealDictCursor
import sqlalchemy
from pydantic import BaseModel
from typing import Optional
import time
from sqlalchemy.orm import Session
from database import get_db,engine
import models
import schema
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/blogs', status_code=status.HTTP_201_CREATED)
def Add_Post(request: schema.Blog,db:Session=Depends(get_db)):
    new_post=models.POST(title=request.title,description=request.description,published=request.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    if not new_post:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Unable to post the data"
        )
    return new_post


@app.get('/blogs', status_code=status.HTTP_200_OK)
def Get_Posts(db:Session=Depends(get_db)):
    posts=db.query(models.POST).all()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found!"
        )

    return posts

@app.get('/blogs{id}',status_code=status.HTTP_200_OK)
def Get_Post_By_ID(id:int,db:Session=Depends(get_db)):
    posts=db.query(models.POST).filter(models.POST.id==id).first()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )

    return posts



@app.put('/blogs{id}',status_code=status.HTTP_200_OK)
def Update_Post_By_ID(id:int,request:schema.Blog,db:Session=Depends(get_db)):
    posts=db.query(models.POST).filter(models.POST.id==id).first()
    posts.title=request.title
    posts.description=request.description
    posts.published=request.published
    db.commit()
    db.refresh(posts)
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )

    return posts


@app.delete('/blogs/{id}', status_code=status.HTTP_200_OK)
def Delete_Post_By_ID(id: int, db: Session = Depends(get_db)):
    post = db.query(models.POST).filter(models.POST.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )
    
    db.delete(post)
    db.commit()
    
    return {"message": f"Post with id={id} has been deleted."}



    
