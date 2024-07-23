from fastapi import FastAPI
from database.database import Base, engine
from database import models

app = FastAPI()


Base.metadata.create_all(engine)


@app.get('/')
async def welcome():
    return 'Welcome To Our Project'
