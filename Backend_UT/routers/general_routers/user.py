from fastapi import APIRouter
from functions import user_functions
from dependencies.dependencies import DB_DEPENDENCY, REDIS_DEPENDENCY, SMS_DEPENDENCY
from dependencies.access_dependencies import USER_DEPENDENCY
from dependencies.body_dependencies import NAME_BODY
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


@router.post('/user_sign_up_phone_verification', status_code=200)
async def user_sign_up_phone_verification(phone_number: NAME_BODY, redis_db: REDIS_DEPENDENCY, db: DB_DEPENDENCY, sms_service: SMS_DEPENDENCY):
    return await user_functions.user_sign_up_phone_verification(phone_number=phone_number, redis_db=redis_db, db=db, sms_service=sms_service)


@router.post('/user_phone_verification_check', status_code=200)
async def user_phone_verification_check(phone_number: NAME_BODY, code: NAME_BODY, redis_db: REDIS_DEPENDENCY):
    return await user_functions.user_phone_verification_check(phone_number=phone_number, code=code, redis_db=redis_db)


@router.post('/user_forget_password', status_code=200)
async def user_forget_password(username: NAME_BODY, redis_db: REDIS_DEPENDENCY, db: DB_DEPENDENCY, sms_service: SMS_DEPENDENCY):
    return await user_functions.user_forget_password(username=username, redis_db=redis_db, db=db, sms_service=sms_service)


@router.post('/user_forget_password_check', status_code=200)
async def user_forget_password_check(username: NAME_BODY, code: NAME_BODY, redis_db: REDIS_DEPENDENCY, db: DB_DEPENDENCY):
    return await user_functions.user_forget_password_check(username=username, code=code, redis_db=redis_db, db=db)