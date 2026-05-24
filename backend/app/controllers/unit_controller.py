from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.unit_schema import UnitCreate
from app.services import unit_service as service

def get_all(db: Session):
    return service.get_all(db)

def get_by_id(db: Session, unit_id: int):
    unit = service.get_by_id(db, unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

def create(db: Session, data: UnitCreate):
    return service.create(db, data)

def update(db: Session, unit_id: int, data: UnitCreate):
    unit = service.update(db, unit_id, data)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

def delete(db: Session, unit_id: int):
    unit = service.delete(db, unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return {"message": "Unit deleted successfully"}