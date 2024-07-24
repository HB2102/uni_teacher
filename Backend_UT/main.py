from fastapi import FastAPI
from database.database import Base, engine
from database import models
from super_admin_routers import super_admin


app = FastAPI(title='Ostad Daneshgah')
app.include_router(super_admin.router)


Base.metadata.create_all(engine)


@app.get('/')
async def welcome():
    return 'Welcome To Our Project'
