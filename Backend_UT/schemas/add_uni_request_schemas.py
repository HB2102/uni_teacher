import datetime
from pydantic import BaseModel


class SendAddUniRequestModel(BaseModel):
    university_names: str
    phone_number: str | None = None
    description: str | None = None


class AddUniRequestDisplay(BaseModel):
    id: int
    university_names: str
    phone_number: str | None = None
    description: str | None = None
    date_added: datetime.datetime
    is_reviewed: bool


    class Config:
        from_attribute = True