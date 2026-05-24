from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitResponse

router = APIRouter(prefix="/units", tags=["Units"])

@router.get("/", response_model=list[UnitResponse])
def get_units(db: Session = Depends(get_db)):
    return db.query(Unit).all()

@router.get("/{unit_id}", response_model=UnitResponse)
def get_unit(unit_id: int, db: Session = Depends(get_db)):
    unit = db.query(Unit).filter(Unit.unit_id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

@router.post("/", response_model=UnitResponse)
def create_unit(unit: UnitCreate, db: Session = Depends(get_db)):
    db_unit = Unit(**unit.model_dump())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@router.put("/{unit_id}", response_model=UnitResponse)
def update_unit(unit_id: int, unit: UnitCreate, db: Session = Depends(get_db)):
    db_unit = db.query(Unit).filter(Unit.unit_id == unit_id).first()
    if not db_unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    for key, value in unit.model_dump().items():
        setattr(db_unit, key, value)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@router.delete("/{unit_id}")
def delete_unit(unit_id: int, db: Session = Depends(get_db)):
    db_unit = db.query(Unit).filter(Unit.unit_id == unit_id).first()
    if not db_unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    db.delete(db_unit)
    db.commit()
    return {"message": "Unit deleted successfully"}