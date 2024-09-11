from fastapi import APIRouter
from functions import subject_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.subject_schemas import SubjectDisplay


router = APIRouter(
    prefix='/admin_subject',
    tags=['Admin Subject'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/add_subject', status_code=201, response_model=SubjectDisplay)
async def add_uni(subject_name: NAME_BODY, db: DB_DEPENDENCY):
    return await subject_functions.add_subject(subject_name=subject_name, db=db)


@router.put('/update_subject', status_code=200, response_model=SubjectDisplay)
async def update_uni(request: SubjectDisplay, db: DB_DEPENDENCY):
    return await subject_functions.update_subject(request=request, db=db)


@router.delete('/delete_subject', status_code=200)
async def delete_subject(subject_id: ID_BODY, db: DB_DEPENDENCY):
    return await subject_functions.delete_subject(subject_id=subject_id, db=db)