from fastapi import APIRouter
from functions import uni_teacher_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/admin_subject',
    tags=['Admin Subject'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/add_uni_teacher', status_code=200)
async def add_uni_teacher(uni_id: ID_BODY, teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await uni_teacher_functions.add_uni_teacher(uni_id=uni_id, teacher_id=teacher_id, db=db)


@router.delete('/delete_uni_teacher', status_code=200)
async def delete_uni_teacher(uni_id: ID_BODY, teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await uni_teacher_functions.delete_uni_teacher(uni_id=uni_id, teacher_id=teacher_id, db=db)


@router.delete('/delete_all_teachers_of_uni', status_code=200)
async def delete_all_teachers_of_uni(uni_id: ID_BODY, db: DB_DEPENDENCY):
    return await uni_teacher_functions.delete_all_teachers_of_uni(uni_id=uni_id, db=db)


@router.delete('/delete_all_unis_of_teacher', status_code=200)
async def delete_all_unis_of_teacher(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await uni_teacher_functions.delete_all_unis_of_teacher(teacher_id=teacher_id, db=db)

