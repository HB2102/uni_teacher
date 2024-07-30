from fastapi import APIRouter
from functions import comment_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from schemas.comment_schema import CommentDisplay


router = APIRouter(
    prefix='/admin_comment',
    tags=['Admin Comment'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.delete('/delete_comment', status_code=200)
async def admin_delete_comment(comment_id: ID_BODY, db: DB_DEPENDENCY):
    return await comment_functions.admin_delete_comment(comment_id=comment_id, db=db)


@router.put('/approve_comment', status_code=200, response_model=CommentDisplay)
async def approve_comment(comment_id: int, db: DB_DEPENDENCY):
    return await comment_functions.approve_comment(comment_id=comment_id, db=db)

