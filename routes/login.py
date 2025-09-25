from fastapi import status,Depends,APIRouter,HTTPException
import models
import schema
from database import get_db
from sqlalchemy.orm import Session
from Credentials import Verify_Pass
from oauth import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(
    tags=["Authenitication"],

)
@router.post('/login',response_model=schema.Token)
def User_Login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.USER).filter(models.USER.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email id not found !!")
    
    if not Verify_Pass(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password !!")
    
    access_token = create_access_token({"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
