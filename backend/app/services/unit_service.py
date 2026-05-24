from sqlalchemy.orm import Session
from app.models.unit_model import Unit
from app.schemas.unit_schema import UnitCreate

def get_all(db: Session):
    return db.query(Unit).all()

def get_by_id(db: Session, unit_id: int):
    return db.query(Unit).filter(Unit.unit_id == unit_id).first()

def create(db: Session, data: UnitCreate):
    unit = Unit(**data.model_dump())
    db.add(unit)
    db.commit()
    db.refresh(unit)
    return unit

def update(db: Session, unit_id: int, data: UnitCreate):
    unit = get_by_id(db, unit_id)
    if not unit:
        return None
    for key, value in data.model_dump().items():
        setattr(unit, key, value)
    db.commit()
    db.refresh(unit)
    return unit

def delete(db: Session, unit_id: int):
    unit = get_by_id(db, unit_id)
    if not unit:
        return None
    db.delete(unit)
    db.commit()
    return unit