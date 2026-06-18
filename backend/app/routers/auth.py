from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_services import user_login
from app.services.student_services import StudentRegister
from sqlalchemy.orm import Session
from app.schemes.student import CreateStudent
from app.core.database import get_db
from app.schemes.student import StudentResponse

router = APIRouter(prefix="/User",tags=["Users"])

@router.post("/register",response_model=StudentResponse)
def Register(data:CreateStudent,db:Session=Depends(get_db)):
    return StudentRegister(db,data)

@router.post("/login")
def login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return user_login(db,data.username,data.password)

@router.post("/my_profile")
def me():
    pass