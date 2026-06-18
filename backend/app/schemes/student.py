from pydantic import BaseModel
from app.schemes.user import UserCreate

class CreateStudent(BaseModel):
    fullname:str
    gender:str
    date_of_birth:str
    admission_number:str
    #user_id:int
    account_information:UserCreate
    class Config:
        from_attributes=True
    
class StudentResponse(BaseModel):
    id:int
    fullname:str
    gender:str
    admission_number:str
    user:UserCreate  
 
    class Config:
        from_attributes=True 