from fastapi import APIRouter, Body
from functions import comment_report_functions
from dependencies.dependencies import DB_DEPENDENCY
from dependencies.access_dependencies import ROUTER_ADMIN_DEPENDENCY
from schemas.comment_report_schemas import ReportDisplay
from typing import Annotated


router = APIRouter(
    prefix='/admin_comment_report',
    tags=['Admin Comment Report'],
    dependencies=[ROUTER_ADMIN_DEPENDENCY]
)

NAME_BODY = Annotated[str, Body(embed=True)]
ID_BODY = Annotated[int, Body(embed=True)]


@router.get('/get_all_reports', status_code=302, response_model=list[ReportDisplay])
async def get_all_reports(db: DB_DEPENDENCY):
    return await comment_report_functions.get_all_reports(db=db)


@router.get('/get_reports_to_review', status_code=302, response_model=list[ReportDisplay])
async def get_reports_to_review(db: DB_DEPENDENCY):
    return await comment_report_functions.get_reports_to_review(db=db)


@router.put('/review_report', status_code=200, response_model=ReportDisplay)
async def review_report(report_id: ID_BODY, db: DB_DEPENDENCY):
    return await comment_report_functions.review_report(report_id=report_id, db=db)
