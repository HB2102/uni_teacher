import datetime
from pydantic import BaseModel, EmailStr
from fastapi import Query
from typing import Optional


class TeacherDisplay(BaseModel):
    full_name: str
    total_average_score: float | None = None
    average_teaching_score: float | None = None
    average_behaviour_score: float | None = None
    average_grading_score : float | None = None
    teacher_pic: str | None = None

    class Config:
        from_attributes = True


class EditTeacherModel(BaseModel):
    id: int
    teacher_new_name: str | None = None
