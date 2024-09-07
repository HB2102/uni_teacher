import datetime
from pydantic import BaseModel, EmailStr


class SendRequestModel(BaseModel):
    text: str
    phone_number: str | None = None


class RequestDisplay(BaseModel):
    id: int
    text: str
    phone_number: str | None = None
    date_added: datetime.datetime
    is_reviewed: bool

    class Config:
        from_attribute = True
