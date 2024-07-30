from fastapi.exceptions import HTTPException
from fastapi import status


NO_RATING_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Rating Found.')