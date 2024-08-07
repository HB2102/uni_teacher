from pydantic import BaseModel


class UniDisplay(BaseModel):
    id: int
    name: str

    class Config:
        from_attribute = True



