from pydantic import BaseModel


class SubjectDisplay(BaseModel):
    id: int
    name: str

    class Config:
        from_attribute = True
