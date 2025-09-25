from fastapi import status,Depends,APIRouter,HTTPException
import models
import schema
from database import get_db
from sqlalchemy.orm import Session
import oauth

router=APIRouter(
    tags=['Posts'],
    prefix='/blogs'
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def Add_Post(request: schema.Blog,db:Session=Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
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


@router.get('/', status_code=status.HTTP_200_OK)
def Get_Posts(db:Session=Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
    posts=db.query(models.POST).all()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found!"
        )

    return posts

@router.get('/{id}',status_code=status.HTTP_200_OK)
def Get_Post_By_ID(id:int,db:Session=Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
    posts=db.query(models.POST).filter(models.POST.id==id).first()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )

    return posts



@router.put('/{id}',status_code=status.HTTP_200_OK)
def Update_Post_By_ID(id:int,request:schema.Blog,db:Session=Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
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


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def Delete_Post_By_ID(id: int, db: Session = Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
    post = db.query(models.POST).filter(models.POST.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )
    
    db.delete(post)
    db.commit()
    
    return {"message": f"Post with id={id} has been deleted."}
