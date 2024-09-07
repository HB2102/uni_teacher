import datetime
from ippanel import Client
from sqlalchemy.orm import Session
from database.models import AddUniRequest
from sms_service.sms_service import SENDER, APPROVE_ADD_UNI_PATTERN, DENY_ADD_UNI_PATTERN
from schemas.add_uni_request_schemas import SendAddUniRequestModel
from errors.add_uni_request_errors import ADD_UNI_REQUEST_NOT_FOUND, NO_ADD_UNI_REQUEST_FOUND


async def send_add_uni_request(request_info: SendAddUniRequestModel, db: Session):
    if request_info.phone_number:
        phone_number = request_info.phone_number
    else:
        phone_number = None

    request = AddUniRequest(
        university_names=request_info.university_names,
        phone_number=phone_number,
        description=request_info.description,
        date_added=datetime.datetime.now(),
    )

    db.add(request)
    db.commit()

    return request


async def get_add_uni_request_by_id(request_id: int, db: Session):
    request = db.query(AddUniRequest).filter(AddUniRequest.id == request_id).first()

    if not request:
        raise ADD_UNI_REQUEST_NOT_FOUND

    return request


async def get_add_uni_request_to_review(db: Session):
    requests = db.query(AddUniRequest).filter(AddUniRequest.is_reviewed == False).order_by(AddUniRequest.date_added.asc()).all()
    if not requests:
        return NO_ADD_UNI_REQUEST_FOUND

    return requests


async def get_all_add_uni_request(db: Session):
    requests = db.query(AddUniRequest).order_by(AddUniRequest.date_added.asc()).all()
    if not requests:
        raise NO_ADD_UNI_REQUEST_FOUND

    return requests


async def search_add_uni_request(request_text: str, db: Session):
    requests = db.query(AddUniRequest).filter(AddUniRequest.university_names.contains(request_text)).all()
    if not requests:
        raise NO_ADD_UNI_REQUEST_FOUND

    return requests


async def get_all_reviewed_add_uni_request(db: Session):
    requests = db.query(AddUniRequest).filter(AddUniRequest.is_reviewed == True).order_by(AddUniRequest.date_added.asc()).all()
    if not requests:
        return NO_ADD_UNI_REQUEST_FOUND

    return requests


async def review_add_uni_request(request_id: int, db: Session):
    request = db.query(AddUniRequest).filter(AddUniRequest.id == request_id).first()

    if not request:
        raise ADD_UNI_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    return request


async def approve_add_uni_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(AddUniRequest).filter(AddUniRequest.id == request_id).first()

    if not request:
        raise ADD_UNI_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send_pattern(
            pattern_code=APPROVE_ADD_UNI_PATTERN,
            sender=SENDER,
            recipient=request.phone_number,
        )

    return request


async def deny_add_uni_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(AddUniRequest).filter(AddUniRequest.id == request_id).first()

    if not request:
        raise ADD_UNI_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send_pattern(
            pattern_code=DENY_ADD_UNI_PATTERN,
            sender=SENDER,
            recipient=request.phone_number,
        )

    return request


async def delete_add_uni_request(request_id: int, db: Session):
    request = db.query(AddUniRequest).filter(AddUniRequest.id == request_id).first()

    if not request:
        raise ADD_UNI_REQUEST_NOT_FOUND

    db.delete(request)
    db.commit()

    return 'Request Deleted.'
