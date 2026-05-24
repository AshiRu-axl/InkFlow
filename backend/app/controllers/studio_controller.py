from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.studio_schema import StudioCreate
from app.services import studio_service as service

def get_all(db: Session):
    return service.get_all(db)

def get_by_id(db: Session, studio_id: int):
    studio = service.get_by_id(db, studio_id)
    if not studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    return studio

def create(db: Session, data: StudioCreate):
    return service.create(db, data)

def update(db: Session, studio_id: int, data: StudioCreate):
    studio = service.update(db, studio_id, data)
    if not studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    return studio

def delete(db: Session, studio_id: int):
    studio = service.delete(db, studio_id)
    if not studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    return {"message": "Studio deleted successfully"}