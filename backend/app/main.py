from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.core.database import Base,engine

Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(auth_router)

