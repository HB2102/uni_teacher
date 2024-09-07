from fastapi.exceptions import HTTPException
from fastapi import status


NO_ADD_UNI_REQUEST_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail='No Add Uni Request Found.')


ADD_UNI_REQUEST_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail='Add Uni Request Not Found.')