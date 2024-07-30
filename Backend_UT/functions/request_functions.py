import datetime
from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Request
from schemas.request_schemas import SendRequestModel
from errors.request_errors import NO_REQUEST_FOUND, REQUEST_NOT_FOUND


async def send_request(request_info: SendRequestModel, db: Session):
    if request_info.email:
        email = request_info.email
    else:
        email = None

    request = Request(
        text=request_info.text,
        email=email,
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

    return request
