from fastapi import status,Depends,APIRouter,HTTPException
import models
import schema
from database import get_db
from sqlalchemy.orm import Session
from Credentials import hash_pass

router=APIRouter()


@router.post('/users')
def create_user(request: schema.User, db: Session = Depends(get_db)):
    existing_user = db.query(models.USER).filter(models.USER.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail="User with this email already exists"
        )

    new_user = models.USER(email=request.email, password=hash_pass(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/users/{id}',response_model=schema.Show_User)
def Get_User(id:int,db:Session=Depends(get_db)):
    user=db.query(models.USER).filter(models.USER.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with this id={id} not found")
    
    return user




    
