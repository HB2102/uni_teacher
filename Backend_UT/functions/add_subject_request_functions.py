import datetime
from ippanel import Client
from sms_service.sms_service import SENDER
from sqlalchemy.orm import Session
from database.models import AddSubjectRequest
from schemas.add_subject_request_schemas import SendAddSubjectRequestModel
from errors.add_subject_request_errors import ADD_SUBJECT_REQUEST_NOT_FOUND, NO_ADD_SUBJECT_REQUEST_FOUND


async def send_add_subject_request(request_info: SendAddSubjectRequestModel, db: Session):
    if request_info.phone_number:
        phone_number = request_info.phone_number
    else:
        phone_number = None

    request = AddSubjectRequest(
        subject_names=request_info.subject_names,
        phone_number=phone_number,
        description=request_info.description,
        date_added=datetime.datetime.now(),
    )

    db.add(request)
    db.commit()

    return request


async def get_add_subject_request_by_id(request_id: int, db: Session):
    request = db.query(AddSubjectRequest).filter(AddSubjectRequest.id == request_id).first()

    if not request:
        raise ADD_SUBJECT_REQUEST_NOT_FOUND

    return request


async def get_add_subject_request_to_review(db: Session):
    requests = db.query(AddSubjectRequest).filter(AddSubjectRequest.is_reviewed == False).order_by(AddSubjectRequest.date_added.asc()).all()
    if not requests:
        return NO_ADD_SUBJECT_REQUEST_FOUND

    return requests


async def get_all_add_subject_request(db: Session):
    requests = db.query(AddSubjectRequest).order_by(AddSubjectRequest.date_added.desc()).all()
    if not requests:
        raise NO_ADD_SUBJECT_REQUEST_FOUND

    return requests


async def search_add_subject_request(request_text: str, db: Session):
    requests = db.query(AddSubjectRequest).filter(AddSubjectRequest.subject_names.contains(request_text)).all()
    if not requests:
        raise NO_ADD_SUBJECT_REQUEST_FOUND

    return requests


async def get_all_reviewed_add_subject_request(db: Session):
    requests = db.query(AddSubjectRequest).filter(AddSubjectRequest.is_reviewed == True).all()
    if not requests:
        return NO_ADD_SUBJECT_REQUEST_FOUND

    return requests


async def review_add_subject_request(request_id: int, db: Session):
    request = db.query(AddSubjectRequest).filter(AddSubjectRequest.id == request_id).first()

    if not request:
        raise ADD_SUBJECT_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    return request


async def approve_add_subject_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(AddSubjectRequest).filter(AddSubjectRequest.id == request_id).first()
    if not request:
        raise ADD_SUBJECT_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send(
            sender=SENDER,
            recipients=[request.phone_number],
            summary='درخواست شما تایید شد.',
            message=f"""
سامانه استاد دانشگاه
درخواست افزودن درس شما پس از بررسی توسط مدیران تایید شد.
با تشکر از همراهی و مشارکت شما.


"""
        )

    return request


async def deny_add_subject_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(AddSubjectRequest).filter(AddSubjectRequest.id == request_id).first()
    if not request:
        raise ADD_SUBJECT_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send(
            sender=SENDER,
            recipients=[request.phone_number],
            summary='درخواست شما رد شد.',
            message=f"""
سامانه استاد دانشگاه
متاسفانه درخواست افزودن درس شما پس از بررسی توسط مدیران مربوطه رد شد.
با تشکر از همراهی و مشارکت شما.


"""

        )

    return request
