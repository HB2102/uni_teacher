from pydantic import BaseModel
from schemas.university_schema import UniDisplay
from schemas.subject_schemas import SubjectDisplay
from schemas.comment_schema import CommentDisplay, CommentDisplayUser
from schemas.rating_schema import RatingDisplay


class TeacherMiniDisplay(BaseModel):
    id: int
    full_name: str


class TeacherDisplay(BaseModel):
    id: int
    full_name: str
    total_average_score: float | None = None
    average_teaching_score: float | None = None
    average_behaviour_score: float | None = None
    average_grading_score : float | None = None
    number_of_comments: int | None = None
    teacher_pic: str | None = None

    class Config:
        from_attributes = True


class EditTeacherModel(BaseModel):
    id: int
    teacher_new_name: str | None = None


class TeacherProfileDisplay(BaseModel):
    teacher: TeacherDisplay
    unis: list[UniDisplay] | None
    subjects: list[SubjectDisplay] | None

    class Config:
        from_attributes = True


class TeacherFullProfileDisplay(TeacherProfileDisplay):
    comments: list[CommentDisplayUser] | None

    class Config:
        from_attributes = True


class TeacherProfileUserDisplay(TeacherProfileDisplay):
    rating: RatingDisplay | None

    class Config:
        from_attributes = True


class TeacherProfileFullUserDisplay(TeacherFullProfileDisplay):
    comments: list[CommentDisplayUser] | None

    class Config:
        from_attributes = True
