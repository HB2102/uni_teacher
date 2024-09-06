from pydantic import BaseModel


class DeletedPicsDisplay(BaseModel):
    id: int
    name: str
    is_reviewed: bool

    class Config:
        from_attributes = True
