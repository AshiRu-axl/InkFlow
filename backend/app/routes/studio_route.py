from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.studio_schema import StudioCreate, StudioResponse
from app.controllers import studio_controller as controller

router = APIRouter(prefix="/studios", tags=["Studios"])

@router.get("/", response_model=list[StudioResponse])
def get_studios(db: Session = Depends(get_db)):
    return controller.get_all(db)

@router.get("/{studio_id}", response_model=StudioResponse)
def get_studio(studio_id: int, db: Session = Depends(get_db)):
    return controller.get_by_id(db, studio_id)

@router.post("/", response_model=StudioResponse)
def create_studio(data: StudioCreate, db: Session = Depends(get_db)):
    return controller.create(db, data)

@router.put("/{studio_id}", response_model=StudioResponse)
def update_studio(studio_id: int, data: StudioCreate, db: Session = Depends(get_db)):
    return controller.update(db, studio_id, data)

@router.delete("/{studio_id}")
def delete_studio(studio_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, studio_id)