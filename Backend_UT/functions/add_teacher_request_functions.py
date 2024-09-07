import datetime
from ippanel import Client
from sqlalchemy.orm import Session
from database.models import AddTeacherRequest
from sms_service.sms_service import SENDER, APPROVE_ADD_TEACHER_PATTERN, DENY_ADD_TEACHER_PATTERN
from schemas.add_teacher_request_schemas import SendAddTeacherRequestModel
from errors.add_teacher_request_error import ADD_TEACHER_REQUEST_NOT_FOUND, NO_ADD_TEACHER_REQUEST_FOUND


async def send_add_teacher_request(request_info: SendAddTeacherRequestModel, db: Session):
    if request_info.phone_number:
        phone_number = request_info.phone_number
    else:
        phone_number = None

    request = AddTeacherRequest(
        teacher_name=request_info.teacher_name,
        phone_number=phone_number,
        uni_text=request_info.uni_text,
        subject_text=request_info.subject_text,
        description=request_info.description,
        date_added=datetime.datetime.now(),
    )

    db.add(request)
    db.commit()
    db.refresh(request)

    return request


async def get_add_teacher_request_by_id(request_id: int, db: Session):
    request = db.query(AddTeacherRequest).filter(AddTeacherRequest.id == request_id).first()

    if not request:
        raise ADD_TEACHER_REQUEST_NOT_FOUND

    return request


async def get_add_teacher_request_to_review(db: Session):
    requests = db.query(AddTeacherRequest).filter(AddTeacherRequest.is_reviewed == False).order_by(AddTeacherRequest.date_added.asc()).all()
    if not requests:
        return NO_ADD_TEACHER_REQUEST_FOUND

    return requests


async def get_all_add_teacher_request(db: Session):
    requests = db.query(AddTeacherRequest).order_by(AddTeacherRequest.date_added.asc()).all()
    if not requests:
        raise NO_ADD_TEACHER_REQUEST_FOUND

    return requests


async def search_add_teacher_request(request_text: str, db: Session):
    requests = db.query(AddTeacherRequest).filter(AddTeacherRequest.teacher_name.contains(request_text)).all()
    if not requests:
        raise NO_ADD_TEACHER_REQUEST_FOUND

    return requests


async def get_all_reviewed_add_teacher_request(db: Session):
    requests = db.query(AddTeacherRequest).filter(AddTeacherRequest.is_reviewed == True).order_by(AddTeacherRequest.date_added.asc()).all()
    if not requests:
        return NO_ADD_TEACHER_REQUEST_FOUND

    return requests


async def review_add_teacher_request(request_id: int, db: Session):
    request = db.query(AddTeacherRequest).filter(AddTeacherRequest.id == request_id).first()
    if not request:
        raise ADD_TEACHER_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.add(request)
    db.commit()
    db.refresh(request)

    return request

async def approve_add_teacher_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(AddTeacherRequest).filter(AddTeacherRequest.id == request_id).first()
    if not request:
        raise ADD_TEACHER_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.add(request)
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send_pattern(
            pattern_code=APPROVE_ADD_TEACHER_PATTERN,
            sender=SENDER,
            recipient=request.phone_number,
        )

    return request


async def deny_add_teacher_request(request_id: int, db: Session, sms_service: Client):
    request = db.query(AddTeacherRequest).filter(AddTeacherRequest.id == request_id).first()
    if not request:
        raise ADD_TEACHER_REQUEST_NOT_FOUND

    request.is_reviewed = True
    db.add(request)
    db.commit()
    db.refresh(request)

    if request.phone_number:
        sms_service.send_pattern(
            pattern_code=DENY_ADD_TEACHER_PATTERN,
            sender=SENDER,
            recipient=request.phone_number,
        )

    return request


async def delete_add_teacher_request(request_id: int, db: Session):
    request = db.query(AddTeacherRequest).filter(AddTeacherRequest.id == request_id).first()
    if not request:
        raise ADD_TEACHER_REQUEST_NOT_FOUND

    db.delete(request)
    db.commit()

    return "Request Deleted."
