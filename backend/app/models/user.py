from app.core.database import Base
from sqlalchemy import  Column,Integer,String,DateTime,Enum,Boolean,DateTime
from datetime import datetime
import enum

class RoleEnum(str,enum.Enum):
    admin="admin"
    teacher="teacher"
    Accountant="Accountant"
    student="dtudent"

class User(Base):
    __tablename__="Users"
    id =Column(Integer,primary_key=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=True)
    role= Column(Enum(RoleEnum),default=RoleEnum.student)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now())