from database.models import User
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session


def check_username_duplicate(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if user:
        return True
    else:
        return False


def check_email_duplicate(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if user:
        return True
    else:
        return False


def check_phone_number_duplicate(phone_number: str, db: Session):
    user = db.query(User).filter(User.phone_number == phone_number).first()

    if user:
        return True
    else:
        return False
