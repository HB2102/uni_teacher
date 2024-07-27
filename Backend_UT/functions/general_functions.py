from database.models import User, University, Subject
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


def check_uni_name_duplicate(uni_name: str, db: Session):
    uni = db.query(University).filter(University.name == uni_name).first()

    if uni:
        return True
    else:
        return False


def check_subject_name_duplicate(subject_name: str, db: Session):
    subject = db.query(Subject).filter(Subject.name == subject_name).first()

    if subject:
        return True
    else:
        return False
