from fastapi.exceptions import HTTPException
from fastapi import status


COMMENT_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                  detail='Comment Not Found.')


NO_COMMENT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail='No Comment Found.')


CANT_DELETE_OTHERS_COMMENT = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                           detail="You Can't Delete Other People's Comments")