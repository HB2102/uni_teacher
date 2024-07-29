from fastapi import APIRouter, Body
from functions import subject_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.subject_schemas import SubjectDisplay
from typing import Annotated


router = APIRouter(
    prefix='/subject',
    tags=['Subject']
)

SUBJECT_ID_BODY = Annotated[int, Body(embed=True)]
SUBJECT_NAME_BODY = Annotated[str, Body(embed=True)]


@router.get('/get_all_subjects', status_code=302, response_model=list[SubjectDisplay])
async def get_all_subjects(db: DB_DEPENDENCY):
    return await subject_functions.get_all_subjects(db=db)


@router.post('/get_subject_by_id', status_code=302, response_model=SubjectDisplay)
async def get_subject_by_id(subjects_id: SUBJECT_ID_BODY, db: DB_DEPENDENCY):
    return await subject_functions.get_subject_by_id(subject_id=subjects_id, db=db)


@router.post('/search_subject', status_code=302, response_model=list[SubjectDisplay])
async def search_subject(subject_name: SUBJECT_NAME_BODY, db: DB_DEPENDENCY):
    return await subject_functions.search_subject_name(subject_name=subject_name, db=db)

