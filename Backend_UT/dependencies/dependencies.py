from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.user_schemas import UserAuth
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from authentication.access import get_current_user, get_current_admin, get_current_super_admin


# Authentication dependencies
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
TOKEN_DEPENDENCY = Annotated[str, Depends(oauth2_scheme)]
AUTHENTICATION_DEPENDENCY = Annotated[OAuth2PasswordRequestForm, Depends()]


# Database dependencies
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]


# Access dependencies
USER_DEPENDENCY = Annotated[UserAuth, Depends(get_current_user)]
ADMIN_DEPENDENCY = Annotated[UserAuth, Depends(get_current_admin)]
SUPER_ADMIN_DEPENDENCY = Annotated[UserAuth, Depends(get_current_super_admin)]
