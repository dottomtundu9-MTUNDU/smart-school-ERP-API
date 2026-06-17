from pydantic import BaseModel,EmailStr,field_validator
from fastapi import HTTPException,status
import re

class User(BaseModel):
    
    email:EmailStr
    password:str
    role:str
    
    @field_validator
    def email_validator(cls,email):
        if not email.endswith("gmail.com"):
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                                detail="email should end with gmail.com")
    @field_validator
    def password_validator(password):
        if len(password)<8:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                                detail="password should contain atleast eight character")   
        if not re.search(r"[0-9]",password):
             raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                                detail="email should contain atleast one integer")  
                     
        if not re.search(r"[A-Z]",password):
             raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                                detail="email should contain atleast one upper later")  
                     
