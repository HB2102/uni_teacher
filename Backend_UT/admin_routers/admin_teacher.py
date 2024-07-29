from fastapi import APIRouter, Body, UploadFile
from functions import teacher_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.teacher_schemas import TeacherDisplay, EditTeacherModel
from typing import Annotated


router = APIRouter(
    prefix='/admin_teacher',
    tags=['Admin Teacher'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)

TEACHER_NAME_BODY = Annotated[str, Body(embed=True)]
TEACHER_ID_BODY = Annotated[int, Body(embed=True)]


@router.post('/add_teacher', status_code=200, response_model=TeacherDisplay)
async def add_teacher(teacher_name: TEACHER_NAME_BODY, db: DB_DEPENDENCY, teacher_pic: UploadFile | None = None):
    return await teacher_functions.add_teacher(teacher_name=teacher_name, db=db, teacher_pic=teacher_pic)


@router.put('/edit_teacher', status_code=200, response_model=TeacherDisplay)
async def edit_teacher(teacher_id: int, db: DB_DEPENDENCY, teacher_new_name: str | None = None, teacher_pic: UploadFile | None = None):
    return await teacher_functions.edit_teacher(teacher_id=teacher_id, teacher_new_name=teacher_new_name, db=db, teacher_pic=teacher_pic)


@router.delete('delete_teacher', status_code=200)
async def delete_teacher(teacher_id: TEACHER_ID_BODY, db: DB_DEPENDENCY):
    return await teacher_functions.delete_teacher(teacher_id=teacher_id, db=db)

