from fastapi import APIRouter, Body
from functions import subject_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ADMIN_DEPENDENCY
from schemas.subject_schemas import SubjectDisplay
from typing import Annotated


router = APIRouter(
    prefix='/admin_subject',
    tags=['Admin Subject']
)

SUBJECT_NAME_BODY = Annotated[str, Body(embed=True)]
SUBJECT_ID_BODY = Annotated[int, Body(embed=True)]


@router.post('/add_subject', status_code=201, response_model=SubjectDisplay)
async def add_uni(subject_name: SUBJECT_NAME_BODY, db: DB_DEPENDENCY, admin: ADMIN_DEPENDENCY):
    return await subject_functions.add_subject(subject_name=subject_name, db=db)


@router.put('/update_subject', status_code=200, response_model=SubjectDisplay)
async def update_uni(request: SubjectDisplay, db: DB_DEPENDENCY, admin: ADMIN_DEPENDENCY):
    return await subject_functions.update_subject(request=request, db=db)


@router.delete('/delete_subject', status_code=200)
async def delete_subject(subject_id: SUBJECT_ID_BODY, db: DB_DEPENDENCY, admin: ADMIN_DEPENDENCY):
    return await subject_functions.delete_uni(subject_id=subject_id, db=db)