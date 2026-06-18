

from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import create_access_token
from app.core.security import Hash



def user_login(db:Session,username:str,password:str):
    user=db.query(User).filter(User.email==username).first()
   
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="wrong email")
    hash_password=Hash.verify_password(password,user.password)    
    if not hash_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="check your password and login again")  
    token= create_access_token({"sub":user.email})   
    return{
        "message":"welcome succesfuly login✅",
        "access_token":token,
        "token_type":"Bearer"
        
    }
