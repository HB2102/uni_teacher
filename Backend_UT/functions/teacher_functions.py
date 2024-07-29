import io
import os
import random
from string import ascii_letters
from urllib.parse import quote

import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
from fastapi import UploadFile
from sqlalchemy.orm import Session
from sqlalchemy import delete
from database.models import Teacher, DeletedPics, Comment, CommentAction, TeacherUni, TeacherSubject, Rating
from errors.teacher_errors import (TEACHER_ALREADY_EXISTS,
                                   UPLOAD_PICTURE_ERROR,
                                   UPLOAD_PICTURE_INTERNAL_ERROR,
                                   TEACHER_NOT_FOUND,
                                   TEACHER_HAS_NO_PICTURE)
from functions.general_functions import check_teacher_name_duplicate


load_dotenv()

LIARA_ENDPOINT = os.getenv("LIARA_ENDPOINT")
LIARA_ACCESS_KEY = os.getenv("LIARA_ACCESS_KEY")
LIARA_SECRET_KEY = os.getenv("LIARA_SECRET_KEY")
LIARA_BUCKET_NAME = os.getenv("LIARA_BUCKET_NAME")


s3 = boto3.client(
    "s3",
    endpoint_url=LIARA_ENDPOINT,
    aws_access_key_id=LIARA_ACCESS_KEY,
    aws_secret_access_key=LIARA_SECRET_KEY,
)


async def add_teacher(teacher_name: str, db: Session, teacher_pic: UploadFile | None = None):
    if check_teacher_name_duplicate(teacher_name, db):
        raise TEACHER_ALREADY_EXISTS

    if teacher_pic:
        rand_str = ''.join(random.choice(ascii_letters) for _ in range(10))
        new_name = f'_{rand_str}.'.join(teacher_pic.filename.rsplit('.', 1))
        teacher_pic.filename = new_name
        try:
            file_content = await teacher_pic.read()
            s3.upload_fileobj(io.BytesIO(file_content), LIARA_BUCKET_NAME, teacher_pic.filename)

        except NoCredentialsError:
            raise UPLOAD_PICTURE_ERROR
        except Exception:
            raise UPLOAD_PICTURE_INTERNAL_ERROR

        filename_encoded = quote(new_name)
        pic_url = f"https://{LIARA_BUCKET_NAME}.{LIARA_ENDPOINT.replace('https://', '')}/{filename_encoded}"

    else:
        pic_url = None
        new_name = None


    teacher = Teacher(
        full_name=teacher_name,
        teacher_pic=pic_url,
        pic_name=new_name
    )

    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    return teacher


async def edit_teacher(teacher_id: int, db: Session, teacher_new_name: str | None = None, teacher_pic: UploadFile | None = None):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    if teacher_new_name:
        if check_teacher_name_duplicate(teacher_new_name, db):
            raise TEACHER_ALREADY_EXISTS

        teacher.full_name = teacher_new_name


    if teacher_pic:
        rand_str = ''.join(random.choice(ascii_letters) for _ in range(10))
        new_name = f'_{rand_str}.'.join(teacher_pic.filename.rsplit('.', 1))
        teacher_pic.filename = new_name
        try:
            file_content = await teacher_pic.read()
            s3.upload_fileobj(io.BytesIO(file_content), LIARA_BUCKET_NAME, teacher_pic.filename)

        except NoCredentialsError:
            raise UPLOAD_PICTURE_ERROR
        except Exception:
            raise UPLOAD_PICTURE_INTERNAL_ERROR

        filename_encoded = quote(new_name)
        pic_url = f"https://{LIARA_BUCKET_NAME}.{LIARA_ENDPOINT.replace('https://', '')}/{filename_encoded}"

        teacher.teacher_pic = pic_url
        if teacher.pic_name:
            old_pic_name = teacher.pic_name

            deletes_pic = DeletedPics(
                name=old_pic_name
            )

            db.add(deletes_pic)

        teacher.pic_name = new_name

    db.commit()

    return teacher


async def delete_teacher(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    comment_ids = db.query(Comment.id).filter(Comment.teacher_id == teacher_id).all()
    delete_comment_actions = delete(CommentAction).where(CommentAction.comment_id.in_(comment_ids))
    db.execute(delete_comment_actions)
    delete_comments = delete(Comment).where(Comment.teacher_id == teacher_id)
    db.execute(delete_comments)
    delete_ratings = delete(Rating).where(Rating.teacher_id == teacher_id)
    db.execute(delete_ratings)
    delete_teacher_uni = delete(TeacherUni).where(TeacherUni.teacher_id == teacher_id)
    db.execute(delete_teacher_uni)
    delete_teacher_subject = delete(TeacherSubject).where(TeacherSubject.teacher_id == teacher_id)
    db.execute(delete_teacher_subject)

    if teacher.teacher_pic:
        delete_pic = DeletedPics(
            name=teacher.pic_name
        )
        db.add(delete_pic)

    db.delete(teacher)
    db.commit()

    return f"Teacher '{teacher.full_name}' Has Been Removed."


async def delete_teacher_pic(teacher_id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    if not teacher.teacher_pic:
        raise TEACHER_HAS_NO_PICTURE

    delete_pic = DeletedPics(
        name=teacher.pic_name
    )
    db.add(delete_pic)

    teacher.teacher_pic = None
    teacher.pic_name = None

    db.commit()

    return f"Picture of '{teacher.full_name}' Has Been Removed."


async def add_teacher_pic(teacher_id: int, db: Session, teacher_pic: UploadFile):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise TEACHER_NOT_FOUND

    rand_str = ''.join(random.choice(ascii_letters) for _ in range(10))
    new_name = f'_{rand_str}.'.join(teacher_pic.filename.rsplit('.', 1))
    teacher_pic.filename = new_name
    try:
        file_content = await teacher_pic.read()
        s3.upload_fileobj(io.BytesIO(file_content), LIARA_BUCKET_NAME, teacher_pic.filename)

    except NoCredentialsError:
        raise UPLOAD_PICTURE_ERROR
    except Exception:
        raise UPLOAD_PICTURE_INTERNAL_ERROR

    filename_encoded = quote(new_name)
    pic_url = f"https://{LIARA_BUCKET_NAME}.{LIARA_ENDPOINT.replace('https://', '')}/{filename_encoded}"

    if teacher.teacher_pic:
        delete_pic = DeletedPics(
            name=teacher.pic_name
        )
        db.add(delete_pic)

    teacher.teacher_pic = pic_url
    teacher.pic_name = new_name

    db.commit()

    return teacher
