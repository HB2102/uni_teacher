from fastapi import APIRouter, Body
from functions import request_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.request_schemas import RequestDisplay
from typing import Annotated


router = APIRouter(
    prefix='/admin_request',
    tags=['Admin Request'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)

NAME_BODY = Annotated[str, Body(embed=True)]
ID_BODY = Annotated[int, Body(embed=True)]


@router.post('/get_request', status_code=302, response_model=RequestDisplay)
async def get_request_by_id(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await request_functions.get_request_by_id(request_id=request_id, db=db)


@router.get('/get_request_to_review', status_code=302, response_model=list[RequestDisplay])
async def get_request_to_review(db: DB_DEPENDENCY):
    return await request_functions.get_requests_to_review(db=db)


@router.get('/get_all_requests', status_code=302, response_model=list[RequestDisplay])
async def get_all_requests(db: DB_DEPENDENCY):
    return await request_functions.get_all_requests(db=db)


@router.post('/search_request', status_code=302, response_model=list[RequestDisplay])
async def search_request(request_text: NAME_BODY, db: DB_DEPENDENCY):
    return await request_functions.search_request(request_text=request_text, db=db)


@router.get('/get_all_reviewed_request', status_code=302, response_model=list[RequestDisplay])
async def get_all_reviewed_request(db: DB_DEPENDENCY):
    return await request_functions.get_all_reviewed_request(db=db)


@router.post('/review_request', status_code=200, response_model=RequestDisplay)
async def review_request(request_id: ID_BODY, db: DB_DEPENDENCY):
    return await request_functions.review_request(request_id=request_id, db=db)