from fastapi import APIRouter, Depends, status
from dependencies.dependencies import AUTHENTICATION_DEPENDENCY, DB_DEPENDENCY
from errors.user_errors import INVALID_USER_ERROR, INVALID_PASSWORD_ERROR
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from database import models
from database.database import get_db
from hash.hash import Hash
from authentication import auth


router = APIRouter(tags=['Authentication'])


@router.post('/token')
def get_token(request: AUTHENTICATION_DEPENDENCY, db: DB_DEPENDENCY):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise INVALID_USER_ERROR

    if not Hash.verify(user.password, request.password):
        raise INVALID_PASSWORD_ERROR

    access_token = auth.create_access_token(data={'sub': user.username})

    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.username,
        'is_admin': user.is_admin,
        'is_super_admin': user.is_super_admin
    }