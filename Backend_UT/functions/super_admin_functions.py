from database.models import User
from sqlalchemy.orm import Session
from schemas.user_schemas import UserModel
from hash.hash import Hash
from functions.general_functions import check_username_duplicate,check_email_duplicate, check_phone_number_duplicate
from errors.user_errors import USER_NAME_DUPLICATE_ERROR, EMAIL_DUPLICATE_ERROR, PHONE_NUMBER_NAME_DUPLICATE_ERROR


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
        is_admin=True,
        is_super_admin=True
    )

    db.add(super_admin)
    db.commit()
    db.refresh(super_admin)

    return super_admin
