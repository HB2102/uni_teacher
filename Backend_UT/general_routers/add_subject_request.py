from fastapi import APIRouter
from functions import add_subject_request_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.add_subject_request_schemas import SendAddSubjectRequestModel, AddSubjectRequestDisplay


router = APIRouter(
    prefix='/add_subject_request',
    tags=['Add Subject Request']
)


@router.post('/send_add_subject_request', status_code=200, response_model=AddSubjectRequestDisplay)
async def send_add_subject_request(request_info: SendAddSubjectRequestModel, db: DB_DEPENDENCY):
    return await add_subject_request_functions.send_add_subject_request(request_info=request_info, db=db)