from fastapi import APIRouter
from functions import add_teacher_request_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.add_teacher_request_schemas import AddTeacherRequestDisplay, SendAddTeacherRequestModel


router = APIRouter(
    prefix='/add_teacher_request',
    tags=['Add Teacher Request']
)


@router.post('/send_add_teacher_request', status_code=200, response_model=AddTeacherRequestDisplay)
async def send_add_teacher_request(request_info: SendAddTeacherRequestModel, db: DB_DEPENDENCY):
    return await add_teacher_request_functions.send_add_teacher_request(request_info=request_info, db=db)