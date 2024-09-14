import time
from fastapi import FastAPI, Request
from database.database import Base, engine
from authentication import authentication_route
from fastapi.middleware.cors import CORSMiddleware
from routers.super_admin_routers import (
    super_admin,
    super_admin_deleted_pics
)
from routers.admin_routers import (
    admin_teacher_subject,
    admin_user,
    admin_rating,
    admin_university,
    admin_comment_report,
    admin_add_uni_request,
    admin_request,
    admin_teacher,
    admin_comment,
    admin_subject,
    admin_uni_teacher,
    admin_add_teacher_request,
    admin_add_subject_request
)
from routers.general_routers import (
    request,
    comment_report,
    add_teacher_request,
    unversity,
    add_uni_request,
    add_subject_request,
    user,
    comment_action,
    rating,
    teacher_subject,
    subject,
    teacher,
    university_teacher,
    comment
)

app = FastAPI(
    title='Ostad Daneshgah',
    debug=True,
)
app.include_router(user.router)
app.include_router(rating.router)
app.include_router(teacher.router)
app.include_router(comment.router)
app.include_router(request.router)
app.include_router(subject.router)
app.include_router(unversity.router)
app.include_router(comment_report.router)
app.include_router(comment_action.router)
app.include_router(teacher_subject.router)
app.include_router(university_teacher.router)
app.include_router(add_subject_request.router)
app.include_router(add_uni_request.router)
app.include_router(add_teacher_request.router)
app.include_router(admin_user.router)
app.include_router(admin_rating.router)
app.include_router(admin_request.router)
app.include_router(admin_comment.router)
app.include_router(admin_subject.router)
app.include_router(admin_teacher.router)
app.include_router(admin_university.router)
app.include_router(admin_uni_teacher.router)
app.include_router(admin_comment_report.router)
app.include_router(admin_teacher_subject.router)
app.include_router(admin_add_subject_request.router)
app.include_router(admin_add_uni_request.router)
app.include_router(admin_add_teacher_request.router)
app.include_router(super_admin.router)
app.include_router(super_admin_deleted_pics.router)
app.include_router(authentication_route.router)

origins = [ 
    "http://localhost:*",
    "http://localhost:5173", 
    "http://localhost:5174",
    "http://127.0.0.1:8000"
] 


app.add_middleware( 
    CORSMiddleware, 
    allow_origins=origins,  # Reflect the allowed origins 
    allow_credentials=True, 
    allow_methods=["*"],  # Allows all methods 
    allow_headers=["*"],  # Allows all headers
)


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



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
        log_level='debug'
    )