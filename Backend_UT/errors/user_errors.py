from fastapi.exceptions import HTTPException
from fastapi import status


USER_NAME_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                          detail='Username Already Exists')


EMAIL_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                      detail='Email Already Exists')


PHONE_NUMBER_NAME_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                                  detail='Phone Number Already Exists')


