from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="john@example.com")
    password: str = Field(..., example="supersecret")

class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    is_admin: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class SweetCreate(BaseModel):
    name: str = Field(..., example="Chocolate")
    category: str = Field(..., example="Candy")
    price: float = Field(..., gt=0, example=10.5)
    quantity: int = Field(..., ge=0, example=5)

class SweetUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)

class SweetOut(BaseModel):
    id: str
    name: str
    category: str
    price: float
    quantity: int

    class Config:
        orm_mode = True


class PurchaseRequest(BaseModel):
    quantity: int = Field(..., gt=0, example=2)


