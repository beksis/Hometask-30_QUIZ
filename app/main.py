# app/main.py

from fastapi import FastAPI
from .routes import router
from .database import engine
from .models import Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(router)
