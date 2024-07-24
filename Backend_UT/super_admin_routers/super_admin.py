from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.user_schemas import SuperAdminDisplay, UserModel
from functions import super_admin_functions
from dependencies.dependencies import DB_DEPENDENCY


router = APIRouter(
    prefix='/super_admin',
    tags=['Super Admin']
)


@router.post('/add_super_admin', status_code=201, response_model=SuperAdminDisplay)
async def add_super_admin(request: UserModel, db: DB_DEPENDENCY):
    return await super_admin_functions.create_super_admin(request=request, db=db)

