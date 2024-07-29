from database.models import User
from sqlalchemy.orm import Session
from sqlalchemy import and_
from schemas.user_schemas import UserModel
from hash.hash import Hash
from functions.general_functions import (check_username_duplicate,
                                         check_email_duplicate,
                                         check_phone_number_duplicate)

from errors.user_errors import (USER_NAME_DUPLICATE_ERROR,
                                EMAIL_DUPLICATE_ERROR,
                                PHONE_NUMBER_NAME_DUPLICATE_ERROR,
                                NO_USER_FOUND_ERROR,
                                USER_NOT_FOUND_ERROR)


async def create_super_admin(request: UserModel, db: Session):
    if check_username_duplicate(request.username, db):
        raise USER_NAME_DUPLICATE_ERROR

    if request.email and check_email_duplicate(request.email, db):
        raise EMAIL_DUPLICATE_ERROR

    if request.phone_number and check_phone_number_duplicate(request.phone_number, db):
        raise PHONE_NUMBER_NAME_DUPLICATE_ERROR

    super_admin = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
        phone_number=request.phone_number,
        is_admin=True,
        is_super_admin=True
    )

    db.add(super_admin)
    db.commit()
    db.refresh(super_admin)

    return super_admin


async def get_all_admins(db: Session):
    users = db.query(User).filter(User.is_admin == True).all()

    if not users:
        raise NO_USER_FOUND_ERROR

    return users


async def search_admin_by_username(user_name: str, db: Session):
    users = db.query(User).filter(and_(User.username.match(user_name), User.is_admin == True)).all()

    if not users:
        raise NO_USER_FOUND_ERROR

    return users


async def promote_to_admin(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if user.is_admin:
        return 'User Is Already Admin'

    user.is_admin = True

    db.commit()

    return f"User '{user.username}' Is Now An Admin."


async def remove_admin_access(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise USER_NOT_FOUND_ERROR

    if not user.is_admin:
        return 'User Is Not Admin'

    user.is_admin = False

    db.commit()

    return f"User '{user.username}' Is Now An Admin."
