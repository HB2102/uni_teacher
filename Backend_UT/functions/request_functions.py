import datetime
from ippanel import Client
from sqlalchemy.orm import Session
from database.models import Request
from schemas.request_schemas import SendRequestModel
from errors.request_errors import NO_REQUEST_FOUND, REQUEST_NOT_FOUND
from sms_service.sms_service import SENDER, APPROVE_REQUEST_PATTERN, DENY_REQUEST_PATTERN


async def send_request(request_info: SendRequestModel, db: Session):
    if request_info.phone_number:
        phone_number = request_info.phone_number
    else:
        phone_number = None

    request = Request(
        text=request_info.text,
        phone_number=phone_number,
        date_added=datetime.datetime.now(),
    )

    db.add(request)
    db.commit()

    return request


async def get_request_by_id(request_id: int, db: Session):
    request = db.query(Request).filter(Request.id == request_id).first()

    if not request:
        raise REQUEST_NOT_FOUND

    return request


async def get_requests_to_review(db: Session):
    requests = db.query(Request).filter(Request.is_reviewed == False).order_by(Request.date_added.desc()).all()
    if not requests:
        return NO_REQUEST_FOUND

    return requests


async def get_all_requests(db: Session):
    requests = db.query(Request).order_by(Request.date_added.desc()).all()
    if not requests:
        raise NO_REQUEST_FOUND

    return requests


async def search_request(request_text: str, db: Session):
    requests = db.query(Request).filter(Request.text.contains(request_text)).all()
    if not requests:
        raise NO_REQUEST_FOUND

    return requests


async def get_all_reviewed_request(db: Session):
    requests = db.query(Request).filter(Request.is_reviewed == True).all()
    if not requests:
        raise NO_REQUEST_FOUND

    return requests


async def review_request(request_id: int, db: Session):
    request = db.query(Request).filter(Request.id == request_id).first()
    if not request:
        raise REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    return request


async def approve_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(Request).filter(Request.id == request_id).first()
    if not request:
        raise REQUEST_NOT_FOUND


    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send_pattern(
            pattern_code=APPROVE_REQUEST_PATTERN,
            sender=SENDER,
            recipient=request.phone_number
        )

    return request


async def deny_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(Request).filter(Request.id == request_id).first()
    if not request:
        raise REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send_pattern(
            pattern_code=DENY_REQUEST_PATTERN,
            sender=SENDER,
            recipient=request.phone_number
        )

    return request