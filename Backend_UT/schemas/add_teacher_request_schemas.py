import datetime
from pydantic import BaseModel


class SendAddTeacherRequestModel(BaseModel):
    teacher_name: str
    phone_number: str | None = None
    uni_text: str | None = None
    subject_text: str | None = None
    description: str | None = None


class AddTeacherRequestDisplay(BaseModel):
    id: int
    teacher_name: str
    phone_number: str | None = None
    uni_text: str | None = None
    subject_text: str | None = None
    description: str | None = None
    date_added: datetime.datetime
    is_reviewed: bool


    class Config:
        from_attribute = True