import bcrypt
from jose import jwt,JWTError
from datetime import datetime,timedelta
from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User,RoleEnum
from app.models.student import Student

SECRET_KEY="SMART_school2026"
ALGORITHM="HS256"
EXPIRE_ACCESS_TOKEN=30

oauth2_schemes=OAuth2PasswordBearer(tokenUrl="/User/login")

#=============TOKEN==============
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now()+timedelta(minutes=EXPIRE_ACCESS_TOKEN)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token
def decode_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="wrong token")
    return payload     

#==================PASSWORD=== HASHING=========
class Hash:
    @staticmethod
    def password_hashing(password):
        pass_byte=password.encode("utf-8")
        salt=bcrypt.gensalt()
        hashed=bcrypt.hashpw(pass_byte,salt)
        return hashed.decode("utf-8")
    
    @staticmethod
    def verify_password(plain_password,hashed_password):
        plain_byte=plain_password.encode("utf-8")
        hashed_byte=hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_byte,hashed_byte)
    
    #===========PROTECT===========ROUTER===============
def get_current_student(token:str=Depends(oauth2_schemes),db:Session=Depends(get_db)):
    payload=decode_token(token)
    email=payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credentials")
    student=db.query(User).filter(User.email==email).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="student not found")
    if not student.is_active:
        raise HTTPException(status_code=status.HTTP_423_LOCKED,detail="account is not active")
    return student

def require_admin(current_student:User=Depends(get_current_student)):
    if current_student.role!=RoleEnum.admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credentials,only admin can acces")
    return current_student

def require_admin_or_student(current_student:User=Depends(get_current_student)):
    if current_student.role not in [RoleEnum.admin,RoleEnum.student]:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credentials")
    return current_student