from fastapi import APIRouter
from functions import add_uni_request_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.add_uni_request_schemas import AddUniRequestDisplay, SendAddUniRequestModel


router = APIRouter(
    prefix='/add_uni_request',
    tags=['Add University Request']
)


@router.post('/send_add_uni_request', status_code=200, response_model=AddUniRequestDisplay)
async def send_add_uni_request(request_info: SendAddUniRequestModel, db: DB_DEPENDENCY):
    return await add_uni_request_functions.send_add_uni_request(request_info=request_info, db=db)