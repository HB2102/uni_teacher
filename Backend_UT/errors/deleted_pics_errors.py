from fastapi.exceptions import HTTPException
from fastapi import status


NO_DELETED_PIC_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                     detail='No Deleted Pic Found.')


DELETED_PIC_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                      detail='Deleted Pic Not Found.')