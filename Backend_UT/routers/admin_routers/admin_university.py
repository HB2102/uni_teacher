from fastapi import APIRouter
from functions import university_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.university_schema import UniDisplay


router = APIRouter(
    prefix='/admin_uni',
    tags=['Admin University'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/add_uni', status_code=201, response_model=UniDisplay)
async def add_uni(uni_name: NAME_BODY, db: DB_DEPENDENCY):
    return await university_functions.add_university(uni_name=uni_name, db=db)


@router.put('/update_uni', status_code=200, response_model=UniDisplay)
async def update_uni(request: UniDisplay, db: DB_DEPENDENCY):
    return await university_functions.update_university(request=request, db=db)


@router.delete('/delete_uni', status_code=200)
async def delete_uni(uni_id: ID_BODY, db: DB_DEPENDENCY):
    return await university_functions.delete_uni(uni_id=uni_id, db=db)