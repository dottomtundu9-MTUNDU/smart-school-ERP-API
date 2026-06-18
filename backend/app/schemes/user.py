from pydantic import BaseModel,EmailStr,field_validator
import re

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    role:str
    
    @field_validator("email")
    def email_validator(cls,email):
        if not email.endswith("gmail.com"):
            raise ValueError("email should end with gmail.com")
        return email
    @field_validator("password")
    def password_validator(cls,password):
        if len(password)<8:
            raise ValueError("password should contain atleast eight character")   
        if not re.search(r"[0-9]",password):
             raise ValueError("password should contain atleast one integer")  
                     
        if not re.search(r"[A-Z]",password):
             raise ValueError("password should contain atleast one upper later")  
        return password     
                     
