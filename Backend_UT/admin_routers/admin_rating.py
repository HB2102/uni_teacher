from fastapi import APIRouter
from functions import rating_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY


router = APIRouter(
    prefix='/admin_rating',
    tags=['Admin Rating'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)


@router.delete('/reset_teacher_ratings', status_code=200)
async def reset_teacher_ratings(teacher_id: ID_BODY, db: DB_DEPENDENCY):
    return await rating_functions.reset_teacher_ratings(teacher_id=teacher_id, db=db)

