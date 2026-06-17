from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_services import user_login
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()
@router.post("/")
def login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return user_login(data.password,data.username,db)