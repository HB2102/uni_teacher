from fastapi import APIRouter
from functions import teacher_subject_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY



router = APIRouter(
    prefix='/admin_subject',
    tags=['Admin Subject'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/add_subject_teacher', status_code=200)
async def add_subject_teacher(subject_id: ID_BODY, teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_subject_functions.add_subject_teacher(subject_id=subject_id, teacher_id=teacher_id, db=db)


@router.delete('/delete_subject_teacher', status_code=200)
async def delete_subject_teacher(subject_id: ID_BODY, teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_subject_functions.delete_subject_teacher(subject_id=subject_id, teacher_id=teacher_id, db=db)


@router.delete('/delete_all_teachers_of_subject', status_code=200)
async def delete_all_teachers_of_subject(subject_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_subject_functions.delete_all_teachers_of_subject(subject_id=subject_id, db=db)


@router.delete('/delete_all_subjects_of_teacher', status_code=200)
async def delete_all_subjects_of_teacher(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_subject_functions.delete_all_subjects_of_teacher(teacher_id=teacher_id, db=db)
