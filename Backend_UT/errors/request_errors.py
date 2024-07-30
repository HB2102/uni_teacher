from fastapi.exceptions import HTTPException
from fastapi import status


NO_REQUEST_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail='No Request Found.')


REQUEST_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                  detail='Request Not Found.')