from fastapi.exceptions import HTTPException
from fastapi import status


COMMENT_ACTION_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                         detail="Comment Action Not Found")