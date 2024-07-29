from fastapi.exceptions import HTTPException
from fastapi import status


UNI_ALREADY_EXISTS_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                         detail='This University Already Exist')


UNI_DONT_EXIST = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                               detail='University Not Found')

NO_UNI_FOUND =HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No University Was Found.')