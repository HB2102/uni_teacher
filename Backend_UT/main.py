from fastapi import FastAPI, Request
from database.database import Base, engine
from database import models
from super_admin_routers import super_admin
from admin_routers import admin_university, admin_subject, admin_user, admin_teacher, admin_uni_teacher, admin_teacher_subject, admin_comment
from general_routers import user, unversity, subject, university_teacher, teacher_subject, comment
from authentication import authentication
import time


app = FastAPI(
    title='Ostad Daneshgah',
    debug=True,
)
app.include_router(comment.router)
app.include_router(admin_comment.router)
app.include_router(teacher_subject.router)
app.include_router(university_teacher.router)
app.include_router(admin_teacher_subject.router)
app.include_router(admin_uni_teacher.router)
app.include_router(subject.router)
app.include_router(unversity.router)
app.include_router(user.router)
app.include_router(admin_user.router)
app.include_router(super_admin.router)
app.include_router(admin_subject.router)
app.include_router(admin_teacher.router)
app.include_router(authentication.router)
app.include_router(admin_university.router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


Base.metadata.create_all(engine)


@app.get('/')
async def welcome():
    return 'Welcome To Our Project'
