from typing import Annotated
from fastapi import Depends
from database.database import get_db
from sqlalchemy.orm import Session


DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
