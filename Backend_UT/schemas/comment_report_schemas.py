import datetime
from pydantic import BaseModel
from schemas.comment_schema import CommentDisplay


class ReportCommentModel(BaseModel):
    comment_id: int
    reason: str | None = None


class ReportCommentDisplay(ReportCommentModel):
    id: int
    date_added: datetime.datetime
    is_reviewed: bool

    class Config:
        from_attribute = True


class ReportDisplay(ReportCommentDisplay):
    comment: CommentDisplay | None = None

    class Config:
        from_attribute = True
