from fastapi import APIRouter
from functions import request_functions
from dependencies.dependencies import DB_DEPENDENCY, SMS_DEPENDENCY
from dependencies.body_dependencies import NAME_BODY, ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.request_schemas import RequestDisplay


router = APIRouter(
    prefix='/admin_request',
    tags=['Admin Request'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/get_request', status_code=200, response_model=RequestDisplay)
async def get_request_by_id(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await request_functions.get_request_by_id(request_id=request_id, db=db)


@router.get('/get_request_to_review', status_code=200, response_model=list[RequestDisplay])
async def get_request_to_review(db: DB_DEPENDENCY):
    return await request_functions.get_requests_to_review(db=db)


@router.get('/get_all_requests', status_code=200, response_model=list[RequestDisplay])
async def get_all_requests(db: DB_DEPENDENCY):
    return await request_functions.get_all_requests(db=db)


@router.post('/search_request', status_code=200, response_model=list[RequestDisplay])
async def search_request(request_text: NAME_BODY, db: DB_DEPENDENCY):
    return await request_functions.search_request(request_text=request_text, db=db)


@router.get('/get_all_reviewed_request', status_code=200, response_model=list[RequestDisplay])
async def get_all_reviewed_request(db: DB_DEPENDENCY):
    return await request_functions.get_all_reviewed_request(db=db)


@router.post('/review_request', status_code=200, response_model=RequestDisplay)
async def review_request(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await request_functions.review_request(request_id=request_id, db=db)


@router.post('/approve_request', status_code=200, response_model=RequestDisplay)
async def approve_request(request_id: ID_BODY, db: DB_DEPENDENCY, sms_service: SMS_DEPENDENCY):
    return await request_functions.approve_request(request_id=request_id, db=db, sms_service=sms_service)


@router.post('/deny_request', status_code=200, response_model=RequestDisplay)
async def deny_request(request_id: ID_BODY, db: DB_DEPENDENCY, sms_service: SMS_DEPENDENCY):
    return await request_functions.deny_request(request_id=request_id, db=db, sms_service=sms_service)


@router.delete('/remove_request', status_code=200)
async def remove_request(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await request_functions.remove_request(request_id=request_id, db=db)