import datetime
from pydantic import BaseModel


class AddCommentModel(BaseModel):
    teacher_id: int
    subject_id: int | None = None
    text: str


class CommentDisplay(BaseModel):
    id: int
    user_id: int
    username: str
    teacher_id: int
    subject_id: int | None = None
    subject_name: str | None = None
    text: str
    date_added: datetime.datetime
    number_of_likes: int
    number_of_dislikes: int
    is_approved: bool

    class Config:
        from_attribute = True


class CommentDisplayUser(CommentDisplay):
    action: bool | None = None

    class Config:
        from_attribute = True


class TeacherCommentRequest(BaseModel):
    teacher_id: int
    order: str | None = None