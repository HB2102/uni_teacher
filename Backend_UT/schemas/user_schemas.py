import datetime
from pydantic import BaseModel, EmailStr
from fastapi import Query
from typing import Optional, List


class UserModel(BaseModel):
    username: str
    password: str
    phone_number: str | None
    email: EmailStr | None


class SuperAdminDisplay(BaseModel):
    id: int
    username: str
    phone_number: str | None
    email: EmailStr | None
    is_admin: bool
    is_super_admin: bool

    class Config:
        from_attributes = True

