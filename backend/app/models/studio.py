from sqlalchemy import Column, Integer, String
from app.database import Base

class Studio(Base):
    __tablename__ = "studio"

    studio_id = Column(Integer, primary_key=True)
    studio_name = Column(String(255), nullable=False)
    phone_number = Column(String(50))

