from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, auth
from ..database import get_db

router = APIRouter(prefix="/api/sweets", tags=["sweets"])

@router.post("", response_model=schemas.SweetOut, status_code=201)
def create_sweet(sweet_in: schemas.SweetCreate, db: Session = Depends(get_db), current_user = Depends(auth.require_admin)):
    # Only admin can create sweets
    return crud.create_sweet(db, sweet_in)

@router.get("", response_model=list[schemas.SweetOut])
def list_sweets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), _=Depends(auth.get_current_user)):
    return crud.get_sweets(db, skip, limit)

@router.get("/search", response_model=list[schemas.SweetOut])
def search_sweets(name: str | None = None, category: str | None = None,
                  min_price: float | None = None, max_price: float | None = None,
                  db: Session = Depends(get_db), _=Depends(auth.get_current_user)):
    return crud.search_sweets(db, name, category, min_price, max_price)

@router.put("/{sweet_id}", response_model=schemas.SweetOut)
def update_sweet(sweet_id: str, upd: schemas.SweetUpdate, db: Session = Depends(get_db), current_user = Depends(auth.require_admin)):
    sweet = crud.get_sweet(db, sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    return crud.update_sweet(db, sweet, upd.dict())

@router.delete("/{sweet_id}", status_code=204)
def delete_sweet(sweet_id: str, db: Session = Depends(get_db), current_user = Depends(auth.require_admin)):
    sweet = crud.get_sweet(db, sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    crud.delete_sweet(db, sweet)
    return

@router.post("/{sweet_id}/purchase", response_model=schemas.SweetOut)
def purchase(sweet_id: str, req: schemas.PurchaseRequest, db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    sweet = crud.get_sweet(db, sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    return crud.purchase_sweet(db, sweet, req.quantity)

@router.post("/{sweet_id}/restock", response_model=schemas.SweetOut)
def restock(sweet_id: str, req: schemas.PurchaseRequest, db: Session = Depends(get_db), current_user = Depends(auth.require_admin)):
    sweet = crud.get_sweet(db, sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    return crud.restock_sweet(db, sweet, req.quantity)
