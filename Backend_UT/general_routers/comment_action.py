from fastapi import APIRouter, Body
from functions import comment_action_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.comment_action_schema import CommentActionModel
from typing import Annotated


router = APIRouter(
    prefix='/comment_action',
    tags=['Comment Action']
)


ID_BODY = Annotated[int, Body(embed=True)]
NAME_BODY = Annotated[str, Body(embed=True)]


@router.post('/like_comment', status_code=200, response_model=CommentActionModel)
async def like_comment(comment_id: ID_BODY, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_action_functions.like_comment(user_id=user.id, comment_id=comment_id, db=db)


@router.post('/dislike_comment', status_code=200, response_model=CommentActionModel)
async def dislike_comment(comment_id: ID_BODY, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_action_functions.dislike_comment(user_id=user.id, comment_id=comment_id, db=db)


@router.put('/remove_like', status_code=200)
async def remove_like(comment_id: ID_BODY, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_action_functions.remove_like(user_id=user.id, comment_id=comment_id, db=db)


@router.put('/remove_dislike', status_code=200)
async def remove_dislike(comment_id: ID_BODY, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_action_functions.remove_dislike(user_id=user.id, comment_id=comment_id, db=db)
