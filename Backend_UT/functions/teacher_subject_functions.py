from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Teacher, Subject, TeacherSubject
from errors.subject_errors import SUBJECT_DONT_EXIST, NO_SUBJECT_FOUND
from errors.teacher_errors import TEACHER_NOT_FOUND, NO_TEACHER_FOUND
from errors.teacher_subject_errors import TEACHER_SUBJECT_NOT_FOUND, TEACHER_SUBJECT_ALREADY_EXIST


async def add_subject_teacher(subject_id: int, teacher_id: int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    teacher_subject_check = db.query(TeacherSubject).filter(and_(TeacherSubject.teacher_id == teacher_id, TeacherSubject.subject_id == subject_id)).first()
    if teacher_subject_check:
        raise TEACHER_SUBJECT_ALREADY_EXIST

    teacher_subject = TeacherSubject(
        teacher_id=teacher_id,
        subject_id=subject_id
    )

    db.add(teacher_subject)
    db.commit()

    return f"Subject '{subject.name}' Added to '{teacher.full_name}'."


async def delete_subject_teacher(subject_id: int, teacher_id: int, db: Session):
    teacher_subject = db.query(TeacherSubject).filter(and_(TeacherSubject.teacher_id == teacher_id, TeacherSubject.subject_id == subject_id)).first()
    if not teacher_subject:
        raise TEACHER_SUBJECT_NOT_FOUND

    db.delete(teacher_subject)
    db.commit()

    return 'Subject Removed From Teacher'


async def delete_all_teachers_of_subject(subject_id: int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    delete_teachers = delete(TeacherSubject).where(TeacherSubject.subject_id == subject_id)
    db.execute(delete_teachers)

    return f"All Teachers of '{subject.name}' Were Removed."


async def delete_all_subjects_of_teacher(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    delete_subjects = delete(TeacherSubject).where(TeacherSubject.teacher_id == teacher_id)
    db.execute(delete_subjects)

    return f"All Subjects of '{teacher.name}' Were Removed."


async def get_all_teachers_of_subject(subject_id: int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    teachers_ids_tuple = db.query(TeacherSubject.teacher_id).filter(TeacherSubject.subject_id == subject_id).all()
    if not teachers_ids_tuple:
        raise NO_TEACHER_FOUND

    teachers_ids = []
    for teachers_id in teachers_ids_tuple:
        teachers_ids.append(teachers_id[0])


    teachers = db.query(Teacher).filter(Teacher.id.in_(teachers_ids))

    if not teachers:
        raise NO_TEACHER_FOUND

    return teachers


async def get_all_subjects_of_teacher(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    subject_ids_tuple = db.query(TeacherSubject.subject_id).filter(TeacherSubject.teacher_id == teacher_id).all()
    if not subject_ids_tuple:
        raise NO_SUBJECT_FOUND

    subject_ids = []
    for subject_id in subject_ids_tuple:
        subject_ids.append(subject_id[0])


    subjects = db.query(Subject).filter(Subject.id.in_(subject_ids))
    if not subjects:
        raise NO_SUBJECT_FOUND

    return subjects
