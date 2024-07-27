import datetime
from pydantic import BaseModel, EmailStr
from fastapi import Query


class UniDisplay(BaseModel):
    id: int
    name: str

    class Config:
        from_attribute = True



