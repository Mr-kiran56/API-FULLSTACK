from fastapi import status,Depends,APIRouter,HTTPException
import models
import schema
from database import get_db
from sqlalchemy.orm import Session
from Credentials import Verify_Pass

router=APIRouter()
@router.post('/login')
def User_Login(request:schema.User,db:Session=Depends(get_db)):
    user=db.query(models.USER).filter(models.USER.email==request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User With this email id not found !!")
    
    if not Verify_Pass(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User With this pass id not found !!")
    return {"token :":"you loginedd !!"}

