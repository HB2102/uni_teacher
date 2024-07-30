from fastapi import APIRouter, Body
from functions import comment_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.comment_schema import CommentDisplay, AddCommentModel, CommentDisplayUser
from typing import Annotated


router = APIRouter(
    prefix='/comment',
    tags=['Comment']
)

ID_BODY = Annotated[int, Body(embed=True)]
NAME_BODY = Annotated[str, Body(embed=True)]


@router.post('/add_comment', status_code=200, response_model=CommentDisplay)
async def add_comment(request: AddCommentModel, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_functions.add_comment(user_id=user.id, request=request, db=db)


@router.delete('/delete_self_comment', status_code=200)
async def delete_self_comment(comment_id: ID_BODY, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_functions.delete_self_comment(user_id=user.id, comment_id=comment_id, db=db)


@router.post('/get_all_comments_of_teacher', status_code=200, response_model=list[CommentDisplay])
async def get_all_comments_of_teacher(teacher_id: ID_BODY, order: NAME_BODY | None, db: DB_DEPENDENCY):
    return await comment_functions.get_all_comments_of_teacher(teacher_id=teacher_id, order=order, db=db)


@router.post('/get_comments_of_teacher_for_user', status_code=200, response_model=list[CommentDisplayUser])
async def get_comments_of_teacher_for_user(teacher_id: ID_BODY, order: NAME_BODY | None, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_functions.get_comments_of_teacher_for_user(teacher_id=teacher_id, order=order, user_id=user.id, db=db)


@router.post('/get_all_self_comments', status_code=200, response_model=list[CommentDisplay])
async def get_all_self_comments(db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await comment_functions.get_all_self_comments(user_id=user.id, db=db)

