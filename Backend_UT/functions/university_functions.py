from sqlalchemy import delete
from sqlalchemy.orm import Session
from database.models import University, TeacherUni, Teacher
from functions.general_functions import check_uni_name_duplicate
from errors.university_errors import UNI_ALREADY_EXISTS_ERROR, UNI_DONT_EXIST, NO_UNI_FOUND
from schemas.university_schema import UniDisplay, BestUniTeacherRequest
from functions.teacher_functions import get_teacher_profile



async def add_university(uni_name: str, db: Session):
    if check_uni_name_duplicate(uni_name, db):
        raise UNI_ALREADY_EXISTS_ERROR

    uni = University(
        name=uni_name
    )

    db.add(uni)
    db.commit()
    db.refresh(uni)

    return uni


async def update_university(request: UniDisplay , db: Session):
    uni = db.query(University).filter(University.id == request.id).first()
    if not uni:
        raise UNI_DONT_EXIST

    if check_uni_name_duplicate(request.name, db):
        raise UNI_ALREADY_EXISTS_ERROR

    uni.name = request.name
    db.commit()

    return uni


async def delete_uni(uni_id: int, db: Session):
    uni = db.query(University).filter(University.id == uni_id).first()
    if not uni:
        raise UNI_DONT_EXIST

    stmt = delete(TeacherUni).where(TeacherUni.university_id == uni_id)
    db.execute(stmt)
    db.delete(uni)
    db.commit()

    return f"'{uni.name}' Has Been Deleted."


async def get_all_uni(db: Session):
    universities = db.query(University).all()
    if not universities:
        raise NO_UNI_FOUND

    return universities


async def get_uni_by_id(uni_id:int, db: Session):
    uni = db.query(University).filter(University.id == uni_id).first()
    if not uni:
        raise UNI_DONT_EXIST

    return uni


async def search_uni_name(uni_name: str, db: Session):
    universities = db.query(University).filter(University.name.match(uni_name)).all()
    if not universities:
        raise NO_UNI_FOUND

    return universities


async def get_best_teachers_of_uni(request: BestUniTeacherRequest, db: Session):
    uni_id = request.uni_id
    uni = db.query(University).filter(University.id == uni_id).first()
    if not uni:
        raise UNI_DONT_EXIST

    teacher_ids_tuple = db.query(TeacherUni.teacher_id).filter(TeacherUni.university_id == uni_id).all()

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
        profile = await get_teacher_profile(teacher_id=teacher.id, db=db)
        if profile:
            teacher_display.append(profile)

    return teacher_display

