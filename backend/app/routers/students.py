from fastapi import APIRouter,Depends
from app.services.student_services import DeleteStudents,get_all,get_by_id,UpdateStudent
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemes.student import StudentResponse,CreateStudent
from app.core.security import require_admin,require_admnin_or_student

router=APIRouter(prefix="/students",tags=["Students"])

@router.get("",response_model=list[StudentResponse])
def getAll(db:Session=Depends(get_db),current_student=Depends(require_admin)):
    return get_all(db)


@router.get("/{id}",response_model=StudentResponse)
def get(id:int,db:Session=Depends(get_db),current_student=Depends(require_admin)):
    return get_by_id(id,db)

@router.put("/{id}")
def getAll(id:int,data:CreateStudent,db:Session=Depends(get_db),current_student=Depends(require_admin)):
    return UpdateStudent(id,data,db)

@router.delete("/{id}")
def getAll(id:int,db:Session=Depends(get_db),current_student=Depends(require_admin)):
    return DeleteStudents(id,db)