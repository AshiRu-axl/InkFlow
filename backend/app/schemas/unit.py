from pydantic import BaseModel

class UnitBase(BaseModel):
    unit_category: str
    name: str
    symbol: str | None = None

class UnitCreate(UnitBase):
    pass

class UnitResponse(UnitBase):
    unit_id: int

    class Config:
        from_attributes = True