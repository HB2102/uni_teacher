from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Rating, Teacher
from schemas.rating_schema import AddRatingModel
from errors.rating_errors import NO_RATING_FOUND
from errors.teacher_errors import TEACHER_NOT_FOUND
from statistics import mean


def update_teacher_rating(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    ratings = db.query(Rating).filter(Rating.teacher_id == teacher_id).all()
    if not ratings:
        teacher.total_average_score = None
        teacher.average_teaching_score = None
        teacher.average_behaviour_score = None
        teacher.average_grading_score = None
        raise NO_RATING_FOUND

    teacher.total_average_score = mean([rating.total_point for rating in ratings])
    teacher.average_teaching_score = mean([rating.teaching_point for rating in ratings])
    teacher.average_behaviour_score = mean([rating.behaviour_point for rating in ratings])
    teacher.average_grading_score = mean([rating.grading_point for rating in ratings])

    db.commit()


async def add_rating(request: AddRatingModel, user_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == request.teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    rating = db.query(Rating).filter(and_(Rating.user_id == user_id, Rating.teacher_id == request.teacher_id)).first()
    if rating:
        rating.total_point = request.total_point
        rating.teaching_point = request.teaching_point
        rating.behaviour_point = request.behaviour_point
        rating.grading_point = request.grading_point
        db.commit()

    else:
        rating = Rating(
            user_id = user_id,
            teacher_id = request.teacher_id,
            total_point = request.total_point,
            teaching_point = request.teaching_point,
            behaviour_point = request.behaviour_point,
            grading_point = request.grading_point
        )
        db.add(rating)

    db.commit()
    update_teacher_rating(teacher_id=request.teacher_id, db=db)

    return rating


async def reset_teacher_ratings(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    ratings = db.query(Rating).filter(Rating.teacher_id == teacher_id).all()
    if not ratings:
        raise NO_RATING_FOUND

    teacher.total_average_score = None
    teacher.average_teaching_score = None
    teacher.average_behaviour_score = None
    teacher.average_grading_score = None

    delete_ratings = delete(Rating).where(Rating.teacher_id == teacher_id)
    db.execute(delete_ratings)

    db.commit()

    return f"Teacher '{teacher.name}' Ratings Has Been Reset"

