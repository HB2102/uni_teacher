from fastapi import APIRouter, Body
from functions import university_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.university_schema import UniDisplay
from typing import Annotated


router = APIRouter(
    prefix='/university',
    tags=['University']
)

UNI_ID_BODY = Annotated[int, Body(embed=True)]
UNI_NAME_BODY = Annotated[str, Body(embed=True)]


@router.get('/get_all_uni', status_code=302, response_model=list[UniDisplay])
async def get_all_uni(db: DB_DEPENDENCY):
    return await university_functions.get_all_uni(db=db)


@router.post('/get_uni_by_id', status_code=302, response_model=UniDisplay)
async def get_uni_by_id(uni_id: UNI_ID_BODY, db: DB_DEPENDENCY):
    return await university_functions.get_uni_by_id(uni_id=uni_id, db=db)


@router.post('/search_uni', status_code=302, response_model=list[UniDisplay])
async def search_uni(uni_name: UNI_NAME_BODY, db: DB_DEPENDENCY):
    return await university_functions.search_uni_name(uni_name=uni_name, db=db)