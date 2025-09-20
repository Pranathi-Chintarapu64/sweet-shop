from fastapi import FastAPI, Depends, HTTPException
from .database import engine, Base, get_db
from .routers import sweets
from .routers import auth as auth_router_module
from . import models, crud, auth
from .config import settings
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sweet Shop API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sweets.router)

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/api/auth/register", response_model=crud.__annotations__.get('create_user', None) or dict, status_code=201)
def register(u: dict, db: Session = Depends(get_db)):
    # we expect json: {"name": "...", "email":"...", "password":"..."}
    data = u
    from .schemas import UserCreate, UserOut
    user_in = UserCreate(**data)
    existing = crud.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db, user_in)
    return user

@app.post("/api/auth/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, req.email)
    if not user or not auth.verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": user.id, "is_admin": user.is_admin})
    return {"access_token": token, "token_type": "bearer"}

app.include_router(sweets.router, prefix="/api")

app = app
