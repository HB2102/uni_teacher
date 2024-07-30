from pydantic import BaseModel, Field


class AddRatingModel(BaseModel):
    teacher_id: int
    total_point: int = Field(gt=0, lt=6)
    teaching_point: int = Field(gt=0, lt=6)
    behaviour_point: int = Field(gt=0, lt=6)
    grading_point: int = Field(gt=0, lt=6)


class RatingDisplay(AddRatingModel):
    user_id: int
