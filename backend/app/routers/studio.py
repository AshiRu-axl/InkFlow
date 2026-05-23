from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Studio
from app.schemas import StudioCreate, StudioResponse

router = APIRouter(
    prefix="/studios",
    tags=["Studios"]
)

@router.get("/", response_model=list[StudioResponse])
def get_studios(db: Session = Depends(get_db)):
    return db.query(Studio).all()

@router.get("/{studio_id}", response_model=StudioResponse)
def get_studio(studio_id: int, db: Session = Depends(get_db)):
    studio = db.query(Studio).filter(Studio.studio_ID == studio_id).first()
    if not studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    return studio

@router.post("/", response_model=StudioResponse)
def create_studio(studio: StudioCreate, db: Session = Depends(get_db)):
    db_studio = Studio(**studio.model_dump())
    db.add(db_studio)
    db.commit()
    db.refresh(db_studio)
    return db_studio

@router.put("/{studio_id}", response_model=StudioResponse)
def update_studio(studio_id: int, studio: StudioCreate, db: Session = Depends(get_db)):
    db_studio = db.query(Studio).filter(Studio.studio_ID == studio_id).first()
    if not db_studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    for key, value in studio.model_dump().items():
        setattr(db_studio, key, value)
    db.commit()
    db.refresh(db_studio)
    return db_studio

@router.delete("/{studio_id}")
def delete_studio(studio_id: int, db: Session = Depends(get_db)):
    db_studio = db.query(Studio).filter(Studio.studio_ID == studio_id).first()
    if not db_studio:
        raise HTTPException(status_code=404, detail="Studio not found")
    db.delete(db_studio)
    db.commit()
    return {"message": "Studio deleted successfully"}