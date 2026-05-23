from pydantic import BaseModel

class StudioBase(BaseModel):
    studio_name: str
    phone_number: str | None = None

class StudioCreate(StudioBase):
    pass

class StudioResponse(StudioBase):
    studio_id: int

    class Config:
        from_attributes = True