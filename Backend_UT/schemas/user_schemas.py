import datetime
from pydantic import BaseModel, EmailStr
from fastapi import Query


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


class UserAuth(BaseModel):
    id: int
    username: str
    email: str | None

    class Config:
        from_attributes = True

