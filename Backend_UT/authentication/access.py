from functions.user_functions import get_user_by_username
from fastapi.responses import JSONResponse
from errors.user_errors import (
    ERROR_CREDENTIAL,
    PROTECTED_ERROR,
    ACCESS_TOKEN_DEMAND_ERROR,
    INVALID_USER_ERROR,
    INVALID_PASSWORD_ERROR,
    REFRESH_TOKEN_DEMAND_ERROR,
    TOKEN_EXPIRED_ERROR,
    INVALID_TOKEN_ERROR
)
from dependencies.dependencies import DB_DEPENDENCY, TOKEN_DEPENDENCY, AUTHENTICATION_DEPENDENCY
from datetime import datetime, timedelta
from database.models import User
from hash.hash import Hash
from jose.exceptions import JWTError
from dotenv import load_dotenv
from jose import jwt
import os


load_dotenv()

SECRET_KEY = os.getenv('AUTHENTICATION_SECRET_KEY')
ALGORITHM = os.getenv('AUTHENTICATION_ALGORITHM')
ACCESS_TOKEN_EXPIRE_DAYS = 1
REFRESH_TOKEN_EXPIRE_DAYS = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None, refresh: bool | None = False):
    to_encode = data.copy()

    if not refresh:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta

        else:
            expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)

    if refresh:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta

        else:
            expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode.update({'exp': expire})
    to_encode.update({'refresh': refresh})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: TOKEN_DEPENDENCY, db: DB_DEPENDENCY):
    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        refresh = _dict.get('refresh')

        if refresh:
            raise ACCESS_TOKEN_DEMAND_ERROR

        if not username:
            raise ERROR_CREDENTIAL

    except JWTError:
        raise ERROR_CREDENTIAL

    user = await get_user_by_username(username, db)

    return user


async def get_current_admin(token: TOKEN_DEPENDENCY, db: DB_DEPENDENCY):
    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        refresh = _dict.get('refresh')

        if refresh:
            raise ACCESS_TOKEN_DEMAND_ERROR

        if not username:
            raise ERROR_CREDENTIAL

    except JWTError:
        raise ERROR_CREDENTIAL

    user = await get_user_by_username(username, db)

    if not user.is_admin:
        raise PROTECTED_ERROR

    return user


async def get_current_super_admin(token: TOKEN_DEPENDENCY, db: DB_DEPENDENCY):
    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        refresh = _dict.get('refresh')

        if refresh:
            raise ACCESS_TOKEN_DEMAND_ERROR

        if not username:
            raise ERROR_CREDENTIAL

    except JWTError:
        raise ERROR_CREDENTIAL

    user = await get_user_by_username(username, db)

    if not user.is_super_admin:
        raise PROTECTED_ERROR

    return user


def login(request: AUTHENTICATION_DEPENDENCY, db: DB_DEPENDENCY):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise INVALID_USER_ERROR

    if not Hash.verify(user.password, request.password):
        raise INVALID_PASSWORD_ERROR

    access_token = create_access_token(data={'sub': user.username})
    refresh_token = create_access_token(data={'sub': user.username}, refresh=True)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'type_token': 'bearer',
        'userID': user.id,
        'username': user.username,
        'is_admin': user.is_admin,
        'is_super_admin': user.is_super_admin
    }


def get_new_access_token(token: TOKEN_DEPENDENCY):
    # try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        refresh = _dict.get('refresh')
        username = _dict.get('sub')

        if not refresh or not username:
            raise REFRESH_TOKEN_DEMAND_ERROR

        expiry_timestamp = _dict.get('exp')

        if not expiry_timestamp:
            raise ERROR_CREDENTIAL

        if datetime.fromtimestamp(expiry_timestamp) < datetime.now():
            raise TOKEN_EXPIRED_ERROR


        new_access_token = create_access_token(data={'sub': username})

        return JSONResponse(content={
            'access_token': new_access_token,
        })

    # except:
    #     raise INVALID_TOKEN_ERROR
