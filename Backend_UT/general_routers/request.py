from fastapi import APIRouter
from functions import request_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.request_schemas import SendRequestModel, RequestDisplay


router = APIRouter(
    prefix='/request',
    tags=['Request']
)


@router.post('/send_request', status_code=200, response_model=RequestDisplay)
async def send_request(request_info: SendRequestModel, db: DB_DEPENDENCY):
    return await request_functions.send_request(request_info=request_info, db=db)

