from sqlalchemy import delete
from sqlalchemy.orm import Session
from database.models import Subject, TeacherSubject
from functions.general_functions import check_subject_name_duplicate
from errors.subject_errors import SUBJECT_ALREADY_EXISTS_ERROR, SUBJECT_DONT_EXIST
from schemas.subject_schemas import SubjectDisplay


async def add_subject(subject_name: str, db: Session):
    if check_subject_name_duplicate(subject_name, db):
        raise SUBJECT_DONT_EXIST

    subject = Subject(
        name=subject_name
    )

    db.add(subject)
    db.commit()
    db.refresh(subject)

    return subject


async def update_subject(request: SubjectDisplay , db: Session):
    subject = db.query(Subject).filter(Subject.id == request.id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    if check_subject_name_duplicate(request.name, db):
        raise SUBJECT_ALREADY_EXISTS_ERROR

    subject.name = request.name
    db.commit()

    return subject


async def delete_uni(subject_id: int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    stmt = delete(TeacherSubject).where(TeacherSubject.subject_id == subject_id)
    db.execute(stmt)
    db.delete(subject)
    db.commit()

    return f"'{subject.name}' Has Been Deleted."

