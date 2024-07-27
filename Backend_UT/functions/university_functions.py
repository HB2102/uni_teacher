from sqlalchemy import delete
from sqlalchemy.orm import Session
from database.models import University, TeacherUni
from functions.general_functions import check_uni_name_duplicate
from errors.university_errors import UNI_ALREADY_EXISTS_ERROR, UNI_DONT_EXIST
from schemas.university_schema import UniDisplay


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

