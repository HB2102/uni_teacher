from fastapi import APIRouter
from functions import teacher_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import USER_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from schemas.teacher_schemas import (
    TeacherProfileDisplay,
    TeacherFullProfileDisplay,
    TeacherProfileUserDisplay,
    TeacherProfileFullUserDisplay
)


router = APIRouter(
    prefix='/teacher',
    tags=['Teacher']
)


@router.post('/search_teacher_name', status_code=302, response_model=list[TeacherProfileDisplay])
async def search_teacher_name(teacher_name: NAME_BODY, db: DB_DEPENDENCY):
    return await teacher_functions.search_teacher_name(teacher_name=teacher_name, db=db)


@router.post('/get_teacher_profile', status_code=200, response_model=TeacherProfileDisplay)
async def get_teacher_profile(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_functions.get_teacher_profile(teacher_id=teacher_id, db=db)


@router.post('/get_teacher_full_profile', status_code=200, response_model=TeacherFullProfileDisplay)
async def get_teacher_full_profile(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_functions.get_teacher_full_profile(teacher_id=teacher_id, db=db)


@router.post('/get_teacher_profile_user', status_code=200, response_model=TeacherProfileUserDisplay)
async def get_teacher_profile_user(teacher_id: ID_BODY, db: DB_DEPENDENCY,  user: USER_DEPENDENCY):
    return await teacher_functions.get_teacher_profile_user(teacher_id=teacher_id, user_id=user.id, db=db)


@router.post('/get_teacher_profile_full_user', status_code=200, response_model=TeacherProfileFullUserDisplay)
async def get_teacher_profile_full_user(teacher_id: ID_BODY, db: DB_DEPENDENCY,  user: USER_DEPENDENCY):
    return await teacher_functions.get_teacher_full_profile_user(teacher_id=teacher_id, user_id=user.id, db=db)



