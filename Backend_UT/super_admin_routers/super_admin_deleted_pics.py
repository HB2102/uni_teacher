from typing import Annotated
from fastapi import APIRouter, Body
from schemas.deleted_pics_schema import DeletedPicsDisplay
from sqlalchemy.orm import Session
from functions import deleted_pictures_function
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_SUPER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/super_admin',
    tags=['Super Admin'],
    dependencies=[ROUTER_SUPER_ADMIN_DEPENDENCY]
)


SUBJECT_NAME_BODY = Annotated[str, Body(embed=True)]
ID_BODY = Annotated[int, Body(embed=True)]


@router.get('/deleted_pics', status_code=302, response_model=list[DeletedPicsDisplay])
async def get_deleted_pics(db: Session = DB_DEPENDENCY):
    return await deleted_pictures_function.get_deleted_pics(db=db)


@router.get('/all_deleted_pics', status_code=302, response_model=list[DeletedPicsDisplay])
async def get_all_deleted_pics(db: Session = DB_DEPENDENCY):
    return await deleted_pictures_function.get_all_deleted_pics(db=db)


@router.put('/review_deleted_pic', status_code=200, response_model=DeletedPicsDisplay)
async def review_deleted_pic(deleted_pic_id: ID_BODY, db: Session = DB_DEPENDENCY):
    return await deleted_pictures_function.review_deleted_pics(deleted_pic_id=deleted_pic_id, db=db)
