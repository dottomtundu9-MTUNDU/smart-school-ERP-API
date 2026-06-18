from app.core.database import Base
from sqlalchemy import  Column,Integer,String,DateTime,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__="Student"
    
    id = Column(Integer,primary_key=True)
    fullname=Column(String,nullable=False)
    gender=Column(String,nullable=False)
    date_of_birth=Column(String,nullable=False)
    admission_number=Column(String,unique=True,nullable=False)
    created_at=Column(DateTime,default=datetime.now())
    
    user_id=Column(Integer,ForeignKey("Users.id"),unique=True,nullable=False)
    
    user=relationship("User",back_populates="student")