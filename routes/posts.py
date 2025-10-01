from fastapi import status,Depends,APIRouter,HTTPException
import models
import schema
from database import get_db
from sqlalchemy.orm import Session
import oauth
from sqlalchemy import or_,func
from typing import List,Optional

router=APIRouter(
    tags=['Posts'],
    prefix='/blogs'
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def Add_Post(request: schema.Blog,db:Session=Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
    new_post=models.POST(title=request.title,description=request.description,published=request.published,owner_id=get_current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    if not new_post:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Unable to post the data"
        )
    return new_post

@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[schema.Vote_Posts])
def Get_Posts(
    db: Session = Depends(get_db),
    get_current_user: int = Depends(oauth.get_current_user),
    limit: int = 10,
    search: Optional[str] = ""
):
    posts = db.query(
        models.POST,
        func.count(models.Votes.post_id).label("votes")
    ).join(
        models.Votes, models.Votes.post_id == models.POST.id, isouter=True
    ).group_by(models.POST.id).limit(limit).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found!"
        )

    return [{"Posts": post, "votes": votes} for post, votes in posts]



@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schema.Post)
def Get_Post_By_ID(id:int,db:Session=Depends(get_db),get_current_user:int=Depends(oauth.get_current_user)):
    posts=db.query(models.POST).filter(models.POST.id==id).first()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )

    return posts



@router.put('/{id}',status_code=status.HTTP_200_OK,response_model=schema.Post)
def Update_Post_By_ID(id:int,request:schema.Blog,db:Session=Depends(get_db),get_current_user: models.USER = Depends(oauth.get_current_user)
                      
):

    posts=db.query(models.POST).filter(models.POST.id==id).first()
    if posts.owner_id != get_current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This post is unauthorized to update"
        )
    

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )
    
    

    posts.title=request.title
    posts.description=request.description
    posts.published=request.published
    db.commit()
    db.refresh(posts)

    return posts


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def Delete_Post_By_ID(id: int, db: Session = Depends(get_db),get_current_user: models.USER = Depends(oauth.get_current_user)
):
    post = db.query(models.POST).filter(models.POST.id == id).first()

    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Data with id={id} not found!"
        )
    
    if post.owner_id != get_current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This post is unauthorized to delete"
        )
    
   

    db.delete(post)
    db.commit()
    
    return {"message": f"Post with id={id} has been deleted."}
