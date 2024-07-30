from pydantic import BaseModel


class CommentActionModel(BaseModel):
    user_id: int
    comment_id: int
    action: bool