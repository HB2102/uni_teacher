import datetime
from pydantic import BaseModel, EmailStr


class SendRequestModel(BaseModel):
    text: str
    email: EmailStr | None = None


class RequestDisplay(BaseModel):
    id: int
    text: str
    email: EmailStr | None = None
    date_added: datetime.datetime
    is_reviewed: bool

    class Config:
        from_attribute = True
