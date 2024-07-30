from fastapi import APIRouter, Body
from functions import rating_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from typing import Annotated


router = APIRouter(
    prefix='/admin_rating',
    tags=['Admin Rating'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)

NAME_BODY = Annotated[str, Body(embed=True)]
ID_BODY = Annotated[int, Body(embed=True)]


@router.delete('/reset_teacher_ratings', status_code=200)
async def reset_teacher_ratings(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await rating_functions.reset_teacher_ratings(teacher_id=teacher_id, db=db)

