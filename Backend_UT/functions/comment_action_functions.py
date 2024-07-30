import datetime
from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Comment, Teacher, User, Subject, CommentAction
from schemas.comment_schema import AddCommentModel
from errors.teacher_errors import TEACHER_NOT_FOUND
from errors.user_errors import USER_NOT_FOUND_ERROR
from errors.comment_errors import COMMENT_NOT_FOUND
from errors.comment_action_errors import COMMENT_ACTION_NOT_FOUND


async def like_comment(user_id: int, comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    comment_action = db.query(CommentAction).filter(and_(CommentAction.user_id == user_id, CommentAction.comment_id == comment_id)).first()
    if comment_action:
        if comment_action.action:
            return comment_action
        else:
            comment_action.action = True
            comment.number_of_likes += 1
            comment.number_of_dislikes -= 1
        db.commit()
        return comment_action

    comment_action = CommentAction(
        user_id=user_id,
        comment_id=comment_id,
        action=True
    )

    comment.number_of_likes += 1

    db.add(comment_action)
    db.commit()

    return comment_action


async def dislike_comment(user_id: int, comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    comment_action = db.query(CommentAction).filter(and_(CommentAction.user_id == user_id, CommentAction.comment_id == comment_id)).first()
    if comment_action:
        if not comment_action.action:
            return comment_action
        else:
            comment_action.action = False
            comment.number_of_dislikes += 1
            comment.number_of_likes -= 1
        db.commit()
        return comment_action

    comment_action = CommentAction(
        user_id=user_id,
        comment_id=comment_id,
        action=False
    )

    comment.number_of_dislikes += 1

    db.add(comment_action)
    db.commit()

    return comment_action


async def remove_like(user_id: int, comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    comment_action = db.query(CommentAction).filter(and_(CommentAction.user_id == user_id, CommentAction.comment_id == comment_id)).first()
    if not comment_action:
        raise COMMENT_ACTION_NOT_FOUND

    db.delete(comment_action)
    comment.number_of_likes -= 1
    db.commit()

    return "Comment Like Removed"


async def remove_dislike(user_id: int, comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    comment_action = db.query(CommentAction).filter(and_(CommentAction.user_id == user_id, CommentAction.comment_id == comment_id)).first()
    if not comment_action:
        raise COMMENT_ACTION_NOT_FOUND

    db.delete(comment_action)
    comment.number_of_dislikes += 1
    db.commit()

    return "Comment Dislike Removed"
