from fastapi import APIRouter
from functions import subject_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.body_dependencies import ID_BODY, NAME_BODY
from schemas.subject_schemas import SubjectDisplay, BestSubjectTeacherRequest
from schemas.teacher_schemas import TeacherProfileDisplay


router = APIRouter(
    prefix='/subject',
    tags=['Subject']
)


@router.get('/get_all_subjects', status_code=200, response_model=list[SubjectDisplay])
async def get_all_subjects(db: DB_DEPENDENCY):
    return await subject_functions.get_all_subjects(db=db)


@router.post('/get_subject_by_id', status_code=200, response_model=SubjectDisplay)
async def get_subject_by_id(subjects_id: ID_BODY, db: DB_DEPENDENCY):
    return await subject_functions.get_subject_by_id(subject_id=subjects_id, db=db)


@router.post('/search_subject', status_code=200, response_model=list[SubjectDisplay])
async def search_subject(subject_name: NAME_BODY, db: DB_DEPENDENCY):
    return await subject_functions.search_subject_name(subject_name=subject_name, db=db)


@router.post('/get_best_teachers_of_subject', status_code=200, response_model=list[TeacherProfileDisplay])
async def get_best_teachers_of_subject(request: BestSubjectTeacherRequest, db: DB_DEPENDENCY):
    return await subject_functions.get_best_teachers_of_subject(request=request, db=db)
