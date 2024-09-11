from fastapi import APIRouter
from functions import rating_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import USER_DEPENDENCY
from schemas.rating_schema import AddRatingModel, RatingDisplay


router = APIRouter(
    prefix='/rating',
    tags=['Rating']
)


@router.post('/add_rating', status_code=200, response_model=RatingDisplay)
async def add_rating(request: AddRatingModel, db: DB_DEPENDENCY, user: USER_DEPENDENCY):
    return await rating_functions.add_rating(request=request, user_id=user.id, db=db)

