from fastapi import APIRouter
from functions import university_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from schemas.university_schema import UniDisplay


router = APIRouter(
    prefix='/university',
    tags=['University']
)


@router.get('/get_all_uni', status_code=200, response_model=list[UniDisplay])
async def get_all_uni(db: DB_DEPENDENCY):
    return await university_functions.get_all_uni(db=db)


@router.post('/get_uni_by_id', status_code=200, response_model=UniDisplay)
async def get_uni_by_id(uni_id: ID_BODY, db: DB_DEPENDENCY):
    return await university_functions.get_uni_by_id(uni_id=uni_id, db=db)


@router.post('/search_uni', status_code=200, response_model=list[UniDisplay])
async def search_uni(uni_name: NAME_BODY, db: DB_DEPENDENCY):
    return await university_functions.search_uni_name(uni_name=uni_name, db=db)