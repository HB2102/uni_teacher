from fastapi.exceptions import HTTPException
from fastapi import status


TEACHER_UNI_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                      detail='This Teacher Is Not in This University')