from fastapi import APIRouter, UploadFile, Form
from functions import teacher_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.teacher_schemas import TeacherDisplay


router = APIRouter(
    prefix='/admin_teacher',
    tags=['Admin Teacher'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/add_teacher', status_code=200, response_model=TeacherDisplay)
async def add_teacher(teacher_name: NAME_BODY, db: DB_DEPENDENCY, teacher_pic: UploadFile | None = None):
    return await teacher_functions.add_teacher(teacher_name=teacher_name, db=db, teacher_pic=teacher_pic)


@router.put('/edit_teacher', status_code=200, response_model=TeacherDisplay)
async def edit_teacher(db: DB_DEPENDENCY, teacher_id: int = Form(...), teacher_new_name: str | None = Form(None), teacher_pic: UploadFile | None = None):
    return await teacher_functions.edit_teacher(teacher_id=teacher_id, teacher_new_name=teacher_new_name, db=db, teacher_pic=teacher_pic)


@router.delete('/delete_teacher', status_code=200)
async def delete_teacher(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_functions.delete_teacher(teacher_id=teacher_id, db=db)


@router.delete('/delete_teacher_pic', status_code=200)
async def delete_teacher_pic(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await teacher_functions.delete_teacher_pic(teacher_id=teacher_id, db=db)


@router.post('/add_teacher_pic', status_code=200, response_model=TeacherDisplay)
async def add_teacher_pic(teacher_id: ID_BODY, db: DB_DEPENDENCY, teacher_pic: UploadFile):
    return await teacher_functions.add_teacher_pic(teacher_id=teacher_id, db=db, teacher_pic=teacher_pic)