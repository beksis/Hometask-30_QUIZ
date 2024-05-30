# app/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from pydantic import BaseModel
from typing import List

router = APIRouter()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserCreate(BaseModel):
    name: str
    phone_number: int
    level: str


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


@router.get("/users/")
async def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get("/questions/")
async def read_questions(db: Session = Depends(get_db)):
    questions = db.query(models.Questions).all()
    return questions


@router.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(
        name=user.name,
        phone_number=user.phone_number,
        level=user.level
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
