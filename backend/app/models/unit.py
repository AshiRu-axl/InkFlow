from sqlalchemy import Column, Integer, String
from app.database import Base

class Unit(Base):
    __tablename__ = "unit"

    unit_id = Column(Integer, primary_key=True)
    unit_category = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    symbol = Column(String(20))