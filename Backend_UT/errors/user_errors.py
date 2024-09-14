from fastapi.exceptions import HTTPException
from fastapi import status


USER_NAME_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                          detail='Username Already Exists.')


EMAIL_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                      detail='Email Already Exists.')


PHONE_NUMBER_DUPLICATE_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                             detail='Phone Number Already Exists.')


USER_NOT_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                     detail='User Not Found.')


ERROR_CREDENTIAL = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                 detail='Invalid Authorization',
                                 headers={'WWW-authenticate': 'bearer'})


TOKEN_EXPIRED_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                    detail='Token Expired.')


INVALID_TOKEN_ERROR = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                    detail='Invalid or Expired Token.')


ACCESS_TOKEN_DEMAND_ERROR = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                          detail='Please Provide Access Token Instead of Refresh Token.')


REFRESH_TOKEN_DEMAND_ERROR = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                           detail='Please Provide Refresh Token Instead of Access Token.')


PROTECTED_ERROR = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Protected.'
                                )


INVALID_USER_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                   detail='Invalid Username.')


INVALID_PASSWORD_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                       detail='Invalid Password.')


DONT_HAVE_ACCESS_ERROR = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                       detail='You Are Forbidden To Change Other Users Info.')


DONT_HAVE_ACCESS_ADMIN_ERROR = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                             detail='You Are Forbidden To Remove An Admin.')


NO_USER_FOUND_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail='No Matched User Was Found')


USER_IS_BANNED = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                               detail='User Has Been Banned.')


USER_PHONE_VERIFICATION_CODE_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                                   detail='User Phone Verification Code Error.')


USER_HAS_NO_PHONE_NUMBER_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                               detail='User Has No Phone Number.')


SMS_SERVER_ERROR = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail='There was an error processing your verification. Try again later.')


USER_VERIFICATION_CODE_EXPIRED_ERROR = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                                     detail='User Verification Code Expired.')