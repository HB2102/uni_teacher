from database.models import User
# from schemas.schemas import UserBase, UpdateUserBase
from sqlalchemy.orm import Session
from errors.user_errors import USER_NOT_FOUND_ERROR
# from database.hash import Hash


def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise USER_NOT_FOUND_ERROR

    return user
