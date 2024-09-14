from fastapi import APIRouter
from dependencies.dependencies import AUTHENTICATION_DEPENDENCY, DB_DEPENDENCY, TOKEN_DEPENDENCY
from authentication import access


router = APIRouter(tags=['Authentication'])


@router.post('/token')
def login(request: AUTHENTICATION_DEPENDENCY, db: DB_DEPENDENCY):
    return access.login(request=request, db=db)


@router.post('/refresh_token')
def get_new_access_token(token: TOKEN_DEPENDENCY):
    return access.get_new_access_token(token=token)


