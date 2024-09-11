from fastapi import APIRouter
from functions import add_subject_request_functions
from dependencies.dependencies import DB_DEPENDENCY, SMS_DEPENDENCY
from dependencies.body_dependencies import NAME_BODY, ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.add_subject_request_schemas import AddSubjectRequestDisplay


router = APIRouter(
    prefix='/admin_add_subject_request',
    tags=['Admin ADD Subject Request'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.post('/get_add_subject_request', status_code=200, response_model=AddSubjectRequestDisplay)
async def get_add_subject_request_by_id(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await add_subject_request_functions.get_add_subject_request_by_id(request_id=request_id, db=db)


@router.get('/get_add_subject_request_to_review', status_code=200, response_model=list[AddSubjectRequestDisplay])
async def get_add_subject_request_to_review(db: DB_DEPENDENCY):
    return await add_subject_request_functions.get_add_subject_request_to_review(db=db)


@router.get('/get_all_add_subject_request', status_code=200, response_model=list[AddSubjectRequestDisplay])
async def get_all_add_subject_request(db: DB_DEPENDENCY):
    return await add_subject_request_functions.get_all_add_subject_request(db=db)


@router.post('/search_add_subject_request', status_code=200, response_model=list[AddSubjectRequestDisplay])
async def search_add_subject_request(request_text: NAME_BODY, db: DB_DEPENDENCY):
    return await add_subject_request_functions.search_add_subject_request(request_text=request_text, db=db)


@router.get('/get_all_reviewed_add_subject_request', status_code=200, response_model=list[AddSubjectRequestDisplay])
async def get_all_reviewed_add_subject_request(db: DB_DEPENDENCY):
    return await add_subject_request_functions.get_all_reviewed_add_subject_request(db=db)


@router.post('/review_add_subject_request', status_code=200, response_model=AddSubjectRequestDisplay)
async def review_add_subject_request(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await add_subject_request_functions.review_add_subject_request(request_id=request_id, db=db)


@router.post('/approve_add_subject_request', status_code=200, response_model=AddSubjectRequestDisplay)
async def approve_add_subject_request(request_id: ID_BODY, db: DB_DEPENDENCY, sms_service: SMS_DEPENDENCY):
    return await add_subject_request_functions.approve_add_subject_request(request_id=request_id, db=db, sms_service=sms_service)


@router.post('/deny_add_subject_request', status_code=200, response_model=AddSubjectRequestDisplay)
async def deny_add_subject_request(request_id: ID_BODY, db: DB_DEPENDENCY, sms_service: SMS_DEPENDENCY):
    return await add_subject_request_functions.deny_add_subject_request(request_id=request_id, db=db, sms_service=sms_service)


@router.delete('/delete_add_subject_request', status_code=200, response_model=AddSubjectRequestDisplay)
async def delete_add_subject_request(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await add_subject_request_functions.remove_add_subject_request(request_id=request_id, db=db)