import bcrypt
from jose import jwt,JWTError
from datetime import datetime,timedelta
from fastapi import HTTPException,status

SECRET_KEY="SMART_school2026"
ALGORITHM="HS256"
EXPIRE_ACCESS_TOKEN=30



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