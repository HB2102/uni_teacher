from functions.user_functions import get_user_by_username
from errors.user_errors import ERROR_CREDENTIAL, PROTECTED_ERROR
from dependencies.dependencies import DB_DEPENDENCY, TOKEN_DEPENDENCY
from datetime import datetime, timedelta
from jose.exceptions import JWTError
from dotenv import load_dotenv
from jose import jwt
import os


load_dotenv()

SECRET_KEY = os.getenv('AUTHENTICATION_SECRET_KEY')
ALGORITHM = os.getenv('AUTHENTICATION_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 3600


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=3600)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: TOKEN_DEPENDENCY, db: DB_DEPENDENCY):
    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')

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

        if not username:
            raise ERROR_CREDENTIAL

    except JWTError:
        raise ERROR_CREDENTIAL

    user = await get_user_by_username(username, db)

    if not user.is_super_admin:
        raise PROTECTED_ERROR

    return user
