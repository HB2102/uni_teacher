from typing import Annotated
from fastapi import Depends
from database.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


DB_DEPENDENCY = Annotated[Session, Depends(get_db)]

TOKEN_DEPENDENCY = Annotated[str, Depends(oauth2_scheme)]
