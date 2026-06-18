from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.students import router as student_router
from app.core.database import Base,engine
Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(auth_router)
app.include_router(student_router)

