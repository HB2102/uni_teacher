from fastapi import APIRouter, Body
from functions import comment_report_functions
from dependencies.dependencies import DB_DEPENDENCY
from schemas.comment_report_schemas import ReportCommentModel, ReportCommentDisplay
from typing import Annotated


router = APIRouter(
    prefix='/comment_report',
    tags=['Comment Report']
)

ID_BODY = Annotated[int, Body(embed=True)]
NAME_BODY = Annotated[str, Body(embed=True)]


@router.post('/add_report', status_code=200, response_model=ReportCommentDisplay)
async def add_report(request: ReportCommentModel, db: DB_DEPENDENCY):
    return await comment_report_functions.add_report(request=request, db=db)