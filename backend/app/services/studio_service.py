from sqlalchemy.orm import Session
from app.models.studio_model import Studio
from app.schemas.studio_schema import StudioCreate

def get_all(db: Session):
    return db.query(Studio).all()

def get_by_id(db: Session, studio_id: int):
    return db.query(Studio).filter(Studio.studio_id == studio_id).first()

def create(db: Session, data: StudioCreate):
    studio = Studio(**data.model_dump())
    db.add(studio)
    db.commit()
    db.refresh(studio)
    return studio

def update(db: Session, studio_id: int, data: StudioCreate):
    studio = get_by_id(db, studio_id)
    if not studio:
        return None
    for key, value in data.model_dump().items():
        setattr(studio, key, value)
    db.commit()
    db.refresh(studio)
    return studio

def delete(db: Session, studio_id: int):
    studio = get_by_id(db, studio_id)
    if not studio:
        return None
    db.delete(studio)
    db.commit()
    return studio