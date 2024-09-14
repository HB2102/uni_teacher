from sqlalchemy import delete
from sqlalchemy.orm import Session
from database.models import Subject, TeacherSubject, Teacher
from functions.general_functions import check_subject_name_duplicate
from errors.subject_errors import SUBJECT_ALREADY_EXISTS_ERROR, SUBJECT_DONT_EXIST, NO_SUBJECT_FOUND
from schemas.subject_schemas import SubjectDisplay, BestSubjectTeacherRequest
from functions.teacher_functions import get_teacher_profile

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


async def delete_subject(subject_id: int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    stmt = delete(TeacherSubject).where(TeacherSubject.subject_id == subject_id)
    db.execute(stmt)
    db.delete(subject)
    db.commit()

    return f"'{subject.name}' Has Been Deleted."


async def get_subject_by_id(subject_id:int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    return subject


async def get_all_subjects(db: Session):
    subjects = db.query(Subject).all()
    if not subjects:
        raise NO_SUBJECT_FOUND

    return subjects


async def search_subject_name(subject_name: str, db: Session):
    subjects = db.query(Subject).filter(Subject.name.match(subject_name)).all()
    if not subjects:
        raise NO_SUBJECT_FOUND

    return subjects


async def get_best_teachers_of_subject(request: BestSubjectTeacherRequest, db: Session):
    subject_id = request.subject_id
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    teacher_ids_tuple = db.query(TeacherSubject.teacher_id).filter(TeacherSubject.subject_id == subject_id).all()

    teacher_ids = []
    for teacher_id in teacher_ids_tuple:
        teacher_ids.append(teacher_id[0])


    if request.limit:
        limit = request.limit
    else:
        limit = 10


    teachers = db.query(Teacher).filter(Teacher.id.in_(teacher_ids)).order_by(Teacher.total_average_score.desc()).limit(limit).all()

    teacher_display = []
    for teacher in teachers:
        teacher_profile = await get_teacher_profile(teacher_id=teacher.id, db=db)
        if teacher_profile:
            teacher_display.append(teacher_profile)

    return teacher_display
