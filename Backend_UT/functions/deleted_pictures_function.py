from sqlalchemy.orm import Session
from database.models import DeletedPics
from errors.deleted_pics_errors import DELETED_PIC_NOT_FOUND, NO_DELETED_PIC_FOUND

async def get_deleted_pics(db: Session):
    deleted_pics = db.query(DeletedPics).filter(DeletedPics.is_reviewed == False).all()
    if not deleted_pics:
        raise NO_DELETED_PIC_FOUND
    return deleted_pics


async def get_all_deleted_pics(db: Session):
    deleted_pics = db.query(DeletedPics).all()
    if not deleted_pics:
        raise NO_DELETED_PIC_FOUND
    return deleted_pics


async def review_deleted_pics(deleted_pic_id: int, db: Session):
    deleted_pic = db.query(DeletedPics).filter(DeletedPics.id == deleted_pic_id).first()
    if not deleted_pic:
        raise DELETED_PIC_NOT_FOUND

    deleted_pic.is_reviewed = True
    db.commit()

    return deleted_pic
