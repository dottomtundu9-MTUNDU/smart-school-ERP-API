from sqlalchemy.orm import  Session
from app.schemes.student import CreateStudent,StudentResponse
from app.models.student import Student
from app.models.user import User
from fastapi import HTTPException,status
from app.core.security import Hash

def StudentRegister(db:Session,data:CreateStudent):
    # existing=db.query(Student).filter(Student.admission_number==data.admission_number).first()
    # if existing:
    hashed_password=Hash.password_hashing(data.account_information.password)    # raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail=f"student with number{adimission_number} already exist")
    user=User(
        email=data.account_information.email,
        password=hashed_password,
        role="student"
    )
    db.add(user)
    db.commit()
    
    student=Student(
        admission_number=data.admission_number,
        fullname=data.fullname,
        date_of_birth=data.date_of_birth,
        gender=data.gender,
        user_id=user.id
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_all(db:Session):
    student=db.query(Student).all()
    return student

def get_by_id(id:int,db:Session):
    student=db.query(Student).filter(Student.id==id).first()
    if not Student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the student with student id {id} not found")
    return student
    

def UpdateStudent(id:int,data:CreateStudent,db:Session):
    student=db.query(Student).filter(Student.id==id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the student with student id {id} not found")
    student.fullname=data.date_of_birth
    student.gender=data.gender
    student.date_of_birth=data.date_of_birth
    db.commit()
    db.refresh(student)
    
    return {"message":f"student with id {id} successfull updated✅✅✅"}

def DeleteStudents(id:int,db:Session):
    student=db.query(Student).filter(Student.id==id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the student with student id {id} not found")
    user=db.query(User).filter(User.id==student.user_id).first()
    db.delete(student)
    if user:
        db.delete(user)
    db.commit()
    return {"message":f"student with id {id} successfull deletes✅✅✅"}
        