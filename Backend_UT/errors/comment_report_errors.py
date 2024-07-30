from fastapi.exceptions import HTTPException
from fastapi import status


NO_REPORT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail='No Report Found.')

REPORT_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail='Report Not Found.')