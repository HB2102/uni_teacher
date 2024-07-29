from fastapi import APIRouter, Body
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY, ADMIN_DEPENDENCY
from schemas.user_schemas import UserDisplay
from typing import Annotated


router = APIRouter(
    prefix='/admin_user',
    tags=['Admin User'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)

USER_ID_BODY = Annotated[int, Body(embed=True)]
USER_NAME_BODY = Annotated[str, Body(embed=True)]


@router.get('/search_users', status_code=302, response_model=list[UserDisplay])
async def search_username(username: USER_NAME_BODY, db: DB_DEPENDENCY):
    return await user_functions.search_user_by_username(user_name=username, db=db)


@router.get('/get_all_users', status_code=302, response_model=list[UserDisplay])
async def get_all_users(db: DB_DEPENDENCY):
    return await user_functions.get_all_users(db=db)


@router.get('/get_user_by_username', status_code=302, response_model=UserDisplay)
async def get_user_by_username(username: USER_NAME_BODY, db: DB_DEPENDENCY):
    return await user_functions.get_user_by_username(username=username, db=db)


@router.get('/get_user_by_id', status_code=302, response_model=UserDisplay)
async def get_user_by_id(user_id: USER_ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.get_user_by_id(user_id=user_id, db=db)


@router.get('/get_all_banned_users', status_code=302, response_model=list[UserDisplay])
async def get_all_banned_users(db: DB_DEPENDENCY):
    return await user_functions.get_all_banned_users(db=db)


@router.delete('/delete_user', status_code=200)
async def admin_delete_user(user_id: USER_ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.admin_delete_user(user_id=user_id, db=db)


@router.put('/ban_user', status_code=200)
async def ban_user(user_id: USER_ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.ban_user(user_id=user_id, db=db)


@router.put('/unban_user', status_code=200)
async def unban_user(user_id: USER_ID_BODY, db: DB_DEPENDENCY):
    return await user_functions.unban_user(user_id=user_id, db=db)