import datetime
from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Comment, Teacher, User, Subject, CommentAction, CommentReport
from schemas.comment_schema import AddCommentModel
from errors.teacher_errors import TEACHER_NOT_FOUND
from errors.user_errors import USER_NOT_FOUND_ERROR, USER_IS_BANNED
from errors.subject_errors import SUBJECT_DONT_EXIST
from errors.comment_errors import COMMENT_NOT_FOUND, CANT_DELETE_OTHERS_COMMENT, NO_COMMENT_FOUND


async def add_comment(user_id: int, request: AddCommentModel, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == request.teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if user.is_banned:
        raise USER_IS_BANNED

    if request.subject_id:
        subject = db.query(Subject).filter(Subject.id == request.subject_id).first()
        if not subject:
            raise SUBJECT_DONT_EXIST
    else:
        request.subject_id = None

    comment = Comment(
        user_id=user_id,
        username=user.username,
        teacher_id=request.teacher_id,
        subject_id=request.subject_id,
        text=request.text,
        date_added=datetime.datetime.now(),
    )

    db.add(comment)

    update_teacher_comment_count(teacher_id=teacher.id, db=db)

    db.commit()

    return comment


async def delete_self_comment(comment_id: int, user_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    if comment.user_id != user_id:
        raise CANT_DELETE_OTHERS_COMMENT



    delete_comment_actions = delete(CommentAction).where(CommentAction.comment_id == comment_id)
    db.execute(delete_comment_actions)
    delete_comment_reports = delete(CommentReport).where(CommentReport.comment_id == comment_id)
    db.execute(delete_comment_reports)

    db.delete(comment)
    db.commit()

    update_teacher_comment_count(teacher_id=comment.teacher_id, db=db)

    return 'Comment Removed Successfully'


async def admin_delete_comment(comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND


    delete_comment_actions = delete(CommentAction).where(CommentAction.comment_id == comment_id)
    db.execute(delete_comment_actions)
    delete_comment_reports = delete(CommentReport).where(CommentReport.comment_id == comment_id)
    db.execute(delete_comment_reports)

    db.delete(comment)
    db.commit()

    update_teacher_comment_count(teacher_id=comment.teacher_id, db=db)

    return 'Comment Removed Successfully'


async def approve_comment(comment_id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    comment.is_approved = True
    db.commit()

    update_teacher_comment_count(teacher_id=comment.teacher_id, db=db)

    return comment


# order means different kinds of comment orders
# newest, oldest, likes, dislikes
async def get_all_comments_of_teacher(teacher_id: int, order: str | None, db: Session) -> list[Comment]:
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    if not order or order == 'newest':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.is_approved == True)).order_by(Comment.date_added.desc()).all()
    elif order == 'oldest':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.is_approved == True)).order_by(Comment.date_added.asc()).all()
    elif order == 'likes':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.is_approved == True)).order_by(Comment.number_of_likes.desc()).all()
    elif order == 'dislikes':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.is_approved == True)).order_by(Comment.number_of_dislikes.desc()).all()
    else:
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.is_approved == True)).all()

    if not comments:
        raise NO_COMMENT_FOUND

    return comments


# order means different kinds of comment orders
# newest, oldest, likes, dislikes
async def get_comments_of_teacher_for_user(teacher_id: int, user_id: int, order: str | None, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if not order or order == 'newest':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.user_id == user_id, Comment.is_approved == True)).order_by(Comment.date_added.desc()).all()

    elif order == 'oldest':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.user_id == user_id, Comment.is_approved == True)).order_by(Comment.date_added.asc()).all()

    elif order == 'likes':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.user_id == user_id, Comment.is_approved == True)).order_by(Comment.number_of_likes.desc()).all()

    elif order == 'dislikes':
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.user_id == user_id, Comment.is_approved == True)).order_by(Comment.number_of_dislikes.desc()).all()
    else:
        comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.user_id == user_id, Comment.is_approved == True)).all()

    if not comments:
        raise NO_COMMENT_FOUND

    for comment in comments:
        comment_action = db.query(CommentAction).filter(CommentAction.comment_id == comment.id).first()
        if comment_action:
            if comment_action.action:
                comment['action'] = True
            else:
                comment['action'] = False
        else:
            comment['action'] = None

    return comments


async def get_comments_to_approve(db: Session):
    comments = db.query(Comment).filter(Comment.is_approved == False).order_by(Comment.date_added.asc()).all()
    if not comments:
        raise NO_COMMENT_FOUND

    return comments


async def get_all_self_comments(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    comments = db.query(Comment).filter(Comment.user_id == user_id).all()
    if not comments:
        raise NO_COMMENT_FOUND

    return comments


def update_teacher_comment_count(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    comments = db.query(Comment).filter(and_(Comment.teacher_id == teacher_id, Comment.is_approved == True)).all()
    if comments:
        number_of_comments = len(comments)
    else:
        number_of_comments = 0

    teacher.number_of_comments = number_of_comments
    db.commit()
