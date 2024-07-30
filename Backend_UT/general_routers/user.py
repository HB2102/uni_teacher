from fastapi import APIRouter
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.user_schemas import UserDisplay, UserModel, UserUpdateModel


router = APIRouter(
    prefix='/user',
    tags=['User']
)



@router.post('/create_user', status_code=201, response_model=UserDisplay)
async def create_user(request: UserModel, db: DB_DEPENDENCY):
    return await user_functions.create_user(request=request, db=db)


@router.put('/update_user', status_code=200, response_model=UserDisplay)
async def update_user(request: UserUpdateModel, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await user_functions.update_user(user_id=user.id, request=request, db=db)


@router.delete('/delete_user', status_code=200)
async def delete_user_self(db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await user_functions.delete_user(user_id=user.id, db=db)



