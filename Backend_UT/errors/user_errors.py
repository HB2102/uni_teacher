from fastapi.exceptions import HTTPException
from fastapi import status


USER_NAME_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                          detail='Username Already Exists')


EMAIL_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                      detail='Email Already Exists')


PHONE_NUMBER_NAME_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                                  detail='Phone Number Already Exists')


USER_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                     detail='User Not Found')


ERROR_CREDENTIAL = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail='Invalid Authorization',
                                 headers={'WWW-authenticate': 'bearer'})


PROTECTED_ERROR = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Protected'
                                )


INVALID_USER_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                   detail='Invalid Username')


INVALID_PASSWORD_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                       detail='Invalid Password')
