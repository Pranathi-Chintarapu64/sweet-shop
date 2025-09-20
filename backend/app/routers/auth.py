from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, auth
from ..database import get_db

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register", response_model=schemas.UserOut, status_code=201)
def register(u: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, u.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db, u)  # default is_admin=False
    return user

@router.post("/login", response_model=schemas.Token)
def login(u: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, u.email, u.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = auth.create_access_token({"sub": str(user.id), "is_admin": user.is_admin})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register-admin", response_model=schemas.UserOut)
def register_admin(u: schemas.UserCreate, db: Session = Depends(get_db), current_user = Depends(auth.require_admin)):
    user = crud.create_user(db, u, is_admin=True)
    return user
