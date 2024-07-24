from typing import Annotated
from fastapi import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


# Authentication dependencies
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
TOKEN_DEPENDENCY = Annotated[str, Depends(oauth2_scheme)]
AUTHENTICATION_DEPENDENCY = Annotated[OAuth2PasswordRequestForm, Depends()]


# Database dependencies
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]


# Access dependencies
