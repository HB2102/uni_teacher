from typing import Annotated
from fastapi import APIRouter, Body
from schemas.user_schemas import UserDisplay, UserModel
from functions import super_admin_functions
from functions.user_functions import delete_user
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_SUPER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/super_admin',
    tags=['Super Admin']
)


USER_NAME_BODY = Annotated[str, Body(embed=True)]
USER_ID_BODY = Annotated[int, Body(embed=True)]


@router.post('/add_super_admin', status_code=201, response_model=UserDisplay)
async def add_super_admin(request: UserModel, db: DB_DEPENDENCY):
    return await super_admin_functions.create_super_admin(request=request, db=db)


@router.get('/get_all_admins', status_code=200, response_model=list[UserDisplay], dependencies=[ROUTER_SUPER_ADMIN_DEPENDENCY])
async def get_all_admins(db: DB_DEPENDENCY):
    return await super_admin_functions.get_all_admins(db=db)


@router.get('/search_admin', status_code=200, response_model=list[UserDisplay], dependencies=[ROUTER_SUPER_ADMIN_DEPENDENCY])
async def search_admin_username(username: USER_NAME_BODY, db: DB_DEPENDENCY):
    return await super_admin_functions.search_admin_by_username(user_name=username, db=db)


@router.delete('/delete_user', status_code=200)
async def super_admin_delete_user(user_id: USER_ID_BODY, db: DB_DEPENDENCY):
    return await delete_user(user_id=user_id, db=db)

