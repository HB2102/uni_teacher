from fastapi.exceptions import HTTPException
from fastapi import status


SUBJECT_ALREADY_EXISTS_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                             detail='This Subject Already Exist')


SUBJECT_DONT_EXIST = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                   detail='Subject Not Found')


NO_SUBJECT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail='No Subject Was Found.')