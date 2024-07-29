from fastapi.exceptions import HTTPException
from fastapi import status


TEACHER_SUBJECT_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                          detail="This Teacher Doesn't Have This University")