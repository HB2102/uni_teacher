from fastapi.exceptions import HTTPException
from fastapi import status


NO_ADD_SUBJECT_REQUEST_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                             detail='No Add Subject Request Found.')


ADD_SUBJECT_REQUEST_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                             detail='Add Subject Request Not Found.')
