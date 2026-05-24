from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.unit_schema import UnitCreate, UnitResponse
from app.controllers import unit_controller as controller

router = APIRouter(prefix="/units", tags=["Units"])

@router.get("/", response_model=list[UnitResponse])
def get_units(db: Session = Depends(get_db)):
    return controller.get_all(db)

@router.get("/{unit_id}", response_model=UnitResponse)
def get_unit(unit_id: int, db: Session = Depends(get_db)):
    return controller.get_by_id(db, unit_id)

@router.post("/", response_model=UnitResponse)
def create_unit(data: UnitCreate, db: Session = Depends(get_db)):
    return controller.create(db, data)

@router.put("/{unit_id}", response_model=UnitResponse)
def update_unit(unit_id: int, data: UnitCreate, db: Session = Depends(get_db)):
    return controller.update(db, unit_id, data)

@router.delete("/{unit_id}")
def delete_unit(unit_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, unit_id)