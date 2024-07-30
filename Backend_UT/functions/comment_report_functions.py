import datetime
from sqlalchemy import delete, and_
from sqlalchemy.orm import Session
from database.models import Comment, CommentReport
from schemas.comment_report_schemas import ReportCommentModel
from errors.comment_errors import COMMENT_NOT_FOUND
from errors.comment_report_errors import NO_REPORT_FOUND, REPORT_NOT_FOUND


async def add_report(request: ReportCommentModel, db: Session):
    comment = db.query(Comment).filter(Comment.id == request.comment_id).first()
    if not comment:
        raise COMMENT_NOT_FOUND

    comment_report = CommentReport(
        comment_id = comment.id,
        reason = request.reason,
        date_added = datetime.datetime.now()
    )

    db.add(comment_report)
    db.commit()
    db.refresh(comment_report)

    return comment_report


async def get_all_reports(db: Session):
    reports = db.query(CommentReport).order_by(CommentReport.date_added.asc()).all()
    if not reports:
        raise NO_REPORT_FOUND

    for report in reports:
        comment = db.query(Comment).filter(Comment.id == report.comment_id).first()
        if comment:
            report['comment'] = comment
        else:
            report['comment'] = None

    return reports


async def get_reports_to_review(db: Session):
    reports = db.query(CommentReport).filter(CommentReport.is_reviewed == False).order_by(CommentReport.date_added.asc()).all()
    if not reports:
        raise NO_REPORT_FOUND

    for report in reports:
        comment = db.query(Comment).filter(Comment.id == report.comment_id).first()
        if comment:
            report['comment'] = comment
        else:
            report['comment'] = None

    return reports


async def review_report(report_id: int, db: Session):
    report = db.query(CommentReport).filter(CommentReport.id == report_id).first()
    if not report:
        raise REPORT_NOT_FOUND

    report.is_reviewed = True
    db.commit()
    db.refresh(report)

    return report
