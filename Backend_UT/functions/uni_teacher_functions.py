from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import University, TeacherUni, Teacher
from errors.university_errors import UNI_DONT_EXIST, NO_UNI_FOUND
from errors.teacher_errors import TEACHER_NOT_FOUND, NO_TEACHER_FOUND
from errors.teacher_uni_errors import TEACHER_UNI_NOT_FOUND


async def add_uni_teacher(uni_id: int, teacher_id: int, db: Session):
    uni = db.query(University).filter(University.id == uni_id).first()
    if not uni:
        raise UNI_DONT_EXIST

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    teacher_uni = TeacherUni(
        teacher_id=teacher_id,
        university_id=uni_id
    )

    db.add(teacher_uni)
    db.commit()

    return f"Teacher '{teacher.full_name}' Added to '{uni.name}'."


async def delete_uni_teacher(uni_id: int, teacher_id: int, db: Session):
    teacher_uni = db.query(TeacherUni).filter(and_(TeacherUni.teacher_id == teacher_id, TeacherUni.university_id == uni_id)).first()
    if not teacher_uni:
        raise TEACHER_UNI_NOT_FOUND

    db.delete(teacher_uni)
    db.commit()

    return 'Teacher Removed From University'


async def delete_all_teachers_of_uni(uni_id: int, db: Session):
    uni = db.query(University).filter(University.id == uni_id).first()
    if not uni:
        raise UNI_DONT_EXIST

    delete_teachers = delete(TeacherUni).where(TeacherUni.university_id == uni_id)
    db.execute(delete_teachers)

    return f"All Teachers of '{uni.name}' Were Removed."


async def delete_all_unis_of_teacher(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    delete_unis = delete(TeacherUni).where(TeacherUni.teacher_id == teacher_id)
    db.execute(delete_unis)

    return f"All Universities of '{teacher.name}' Were Removed."


async def get_all_teachers_of_university(uni_id: int, db: Session):
    uni = db.query(University).filter(University.id == uni_id).first()
    if not uni:
        raise UNI_DONT_EXIST

    teachers_ids = db.query(TeacherUni.teacher_id).filter(TeacherUni.university_id == uni_id).all()
    teachers = db.query(Teacher).filter(Teacher.id.in_(teachers_ids))

    if not teachers:
        raise NO_TEACHER_FOUND

    return teachers


async def get_all_unis_of_teacher(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    uni_ids = db.query(TeacherUni.university_id).filter(TeacherUni.teacher_id == teacher_id).all()
    unis = db.query(University).filter(University.id.in_(uni_ids))

    if not unis:
        raise NO_UNI_FOUND

    return unis
