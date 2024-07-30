from database.models import User, Comment, CommentAction, Rating
from sqlalchemy.orm import Session
from sqlalchemy import delete
from hash.hash import Hash
from schemas.user_schemas import UserModel, UserUpdateModel
from errors.user_errors import (
    USER_NOT_FOUND_ERROR,
    USER_NAME_DUPLICATE_ERROR,
    EMAIL_DUPLICATE_ERROR,
    PHONE_NUMBER_NAME_DUPLICATE_ERROR,
    DONT_HAVE_ACCESS_ERROR,
    NO_USER_FOUND_ERROR,
    DONT_HAVE_ACCESS_ADMIN_ERROR
)
from functions.general_functions import (
    check_username_duplicate,
    check_phone_number_duplicate,
    check_email_duplicate
)


async def get_all_users(db: Session):
    users = db.query(User).all()

    if not users:
        raise NO_USER_FOUND_ERROR

    return users


async def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user


async def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user


async def create_user(request: UserModel, db: Session):
    if check_username_duplicate(request.username, db):
        raise USER_NAME_DUPLICATE_ERROR

    if request.email and check_email_duplicate(request.email, db):
        raise EMAIL_DUPLICATE_ERROR

    if request.phone_number and check_phone_number_duplicate(request.phone_number, db):
        raise PHONE_NUMBER_NAME_DUPLICATE_ERROR

    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
        phone_number=request.phone_number,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


async def update_user(user_id: int, request: UserUpdateModel, db: Session):
    user = db.query(User).filter(User.id == request.id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if user_id != request.id:
        raise DONT_HAVE_ACCESS_ERROR

    if request.username:
        if check_username_duplicate(request.username, db):
            raise USER_NAME_DUPLICATE_ERROR

        user.username = request.username

    if request.email:
        if check_email_duplicate(request.email, db):
            raise EMAIL_DUPLICATE_ERROR

        user.email = request.email

    if request.phone_number:
        if check_phone_number_duplicate(request.phone_number, db):
            raise PHONE_NUMBER_NAME_DUPLICATE_ERROR

        user.email = request.email

    if request.password:
        user.password = Hash.bcrypt(request.password)

    db.commit()

    return user


async def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    delete_comment_actions = delete(CommentAction).where(CommentAction.user_id == user_id)
    delete_comments = delete(Comment).where(Comment.user_id == user_id)
    delete_ratings = delete(Rating).where(Rating.user_id == user_id)

    db.execute(delete_comment_actions)
    db.execute(delete_comments)
    db.execute(delete_ratings)

    db.delete(user)
    db.commit()
    return f"User '{user.username}' Has Been Deleted"


async def admin_delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if user.is_admin or user.is_super_admin:
        raise DONT_HAVE_ACCESS_ADMIN_ERROR

    return delete_user(user_id=user_id, db=db)


async def ban_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if user.is_banned:
        return 'User Is Already Banned.'

    user.is_banned = True

    db.commit()

    return f"User '{user.username}' Banned By Admin."


async def unban_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if not user.is_banned:
        return 'User Is Not Banned.'

    user.is_banned = False

    db.commit()

    return f"User '{user.username}' Unbanned By Admin."


async def search_user_by_username(user_name: str, db: Session):
    users = db.query(User).filter(User.username.match(user_name)).all()

    if not users:
        raise NO_USER_FOUND_ERROR

    return users


async def get_all_banned_users(db: Session):
    users = db.query(User).filter(User.is_banned == True).all()

    if not users:
        raise NO_USER_FOUND_ERROR

    return users
