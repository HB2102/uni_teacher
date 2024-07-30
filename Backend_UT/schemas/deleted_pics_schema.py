from pydantic import BaseModel


class DeletedPicsDisplay(BaseModel):
    id: int
    pic_name: str
    is_reviewed: bool

    class Config:
        orm_mode = True
