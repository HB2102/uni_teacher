from fastapi.exceptions import HTTPException
from fastapi import status


NO_ADD_TEACHER_REQUEST_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                             detail='No Add Teacher Request Found.')


ADD_TEACHER_REQUEST_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                              detail='Add Teacher Request Not Found.')