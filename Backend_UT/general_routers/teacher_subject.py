from fastapi import APIRouter, Body
from functions import teacher_subject_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.teacher_schemas import TeacherDisplay
from schemas.subject_schemas import SubjectDisplay
from typing import Annotated


router = APIRouter(
    prefix='/teacher_subject',
    tags=['Subject Teacher']
)


ID_BODY = Annotated[int, Body(embed=True)]
NAME_BODY = Annotated[str, Body(embed=True)]


@router.post('/get_all_teachers_of_subject', status_code=200, response_model=list[TeacherDisplay])
async def get_all_teachers_of_subject(subject_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_subject_functions.get_all_teachers_of_subject(subject_id=subject_id, db=db)


@router.post('/get_all_subjects_of_teacher', status_code=200, response_model=list[SubjectDisplay])
async def get_all_subjects_of_teacher(teacher_id, db: DB_DEPENDENCY):
    return await teacher_subject_functions.get_all_subjects_of_teacher(teacher_id=teacher_id, db=db)