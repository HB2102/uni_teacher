from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Teacher, Subject, TeacherSubject
from errors.subject_errors import SUBJECT_DONT_EXIST
from errors.teacher_errors import TEACHER_NOT_FOUND
from errors.teacher_subject_errors import TEACHER_SUBJECT_NOT_FOUND


async def add_subject_teacher(subject_id: int, teacher_id: int, db: Session):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise SUBJECT_DONT_EXIST

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

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