from sqlalchemy.orm import Session
from . import models, schemas, auth
from sqlalchemy import or_, and_
from decimal import Decimal

def create_user(db: Session, user_in: schemas.UserCreate, is_admin: bool = False):
    hashed = auth.hash_password(user_in.password)
    user = models.User(name=user_in.name, email=user_in.email, password_hash=hashed, is_admin=is_admin)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_sweet(db: Session, sweet_in: schemas.SweetCreate):
    sweet = models.Sweet(name=sweet_in.name, category=sweet_in.category, price=Decimal(str(sweet_in.price)), quantity=sweet_in.quantity)
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

def get_sweets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sweet).offset(skip).limit(limit).all()

def get_sweet(db: Session, sweet_id: str):
    return db.query(models.Sweet).filter(models.Sweet.id == sweet_id).first()

def search_sweets(db: Session, name=None, category=None, min_price=None, max_price=None):
    q = db.query(models.Sweet)
    if name:
        q = q.filter(models.Sweet.name.ilike(f"%{name}%"))
    if category:
        q = q.filter(models.Sweet.category.ilike(f"%{category}%"))
    if min_price is not None:
        q = q.filter(models.Sweet.price >= Decimal(str(min_price)))
    if max_price is not None:
        q = q.filter(models.Sweet.price <= Decimal(str(max_price)))
    return q.all()

def update_sweet(db: Session, sweet: models.Sweet, data: dict):
    for k,v in data.items():
        if v is None: continue
        setattr(sweet, k, v)
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

def delete_sweet(db: Session, sweet: models.Sweet):
    db.delete(sweet)
    db.commit()

def purchase_sweet(db: Session, sweet: models.Sweet, qty: int):
    if sweet.quantity < qty:
        raise ValueError("Not enough quantity")
    sweet.quantity -= qty
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

def restock_sweet(db: Session, sweet: models.Sweet, qty: int):
    sweet.quantity += qty
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet
