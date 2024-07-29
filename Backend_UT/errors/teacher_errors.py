from fastapi.exceptions import HTTPException
from fastapi import status


TEACHER_ALREADY_EXISTS = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                       detail='Teacher Already Exists.')

UPLOAD_PICTURE_ERROR = HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                     detail='Upload Picture Is Not Possible Due To Service Error')


UPLOAD_PICTURE_INTERNAL_ERROR = HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                              detail='There Was A Problem Uploading Picture, Try Again Later.')


TEACHER_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                  detail='Teacher Not Found.')


NO_TEACHER_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail='No Teacher Was Found.')


TEACHER_HAS_NO_PICTURE = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                       detail='Teacher Has No Picture.')