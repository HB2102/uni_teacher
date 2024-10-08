from fastapi import APIRouter
from functions import uni_teacher_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from schemas.teacher_schemas import TeacherDisplay
from schemas.university_schema import UniDisplay


router = APIRouter(
    prefix='/teacher_uni',
    tags=['University Teacher']
)


@router.post('/get_all_teachers_of_university', status_code=200, response_model=list[TeacherDisplay])
async def get_all_teachers_of_university(uni_id: ID_BODY, db: DB_DEPENDENCY):
    return await uni_teacher_functions.get_all_teachers_of_university(uni_id=uni_id, db=db)


@router.post('/get_all_unis_of_teacher', status_code=200, response_model=list[UniDisplay])
async def get_all_unis_of_teacher(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await uni_teacher_functions.get_all_unis_of_teacher(teacher_id=teacher_id, db=db)