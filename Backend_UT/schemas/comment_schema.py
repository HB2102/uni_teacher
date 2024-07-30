import datetime
from pydantic import BaseModel


class AddCommentModel(BaseModel):
    teacher_id: int
    subject_id: int | None = None
    text: str


class CommentDisplay(BaseModel):
    user_id: int
    username: str
    teacher_id: int
    subject_id: int | None = 0
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
