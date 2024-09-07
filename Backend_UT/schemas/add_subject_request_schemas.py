import datetime
from pydantic import BaseModel


class SendAddSubjectRequestModel(BaseModel):
    subject_names: str
    phone_number: str | None = None
    description: str | None = None


class AddSubjectRequestDisplay(BaseModel):
    id: int
    subject_names: str
    phone_number: str | None = None
    description: str | None = None
    date_added: datetime.datetime
    is_reviewed: bool


    class Config:
        from_attribute = True
