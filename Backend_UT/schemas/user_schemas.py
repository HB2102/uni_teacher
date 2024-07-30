from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    username: str
    password: str
    phone_number: str | None = None
    email: EmailStr | None = None


class UserDisplay(BaseModel):
    id: int
    username: str
    phone_number: str | None = None
    email: EmailStr | None = None
    is_admin: bool
    is_super_admin: bool
    is_banned: bool

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str | None = None

    class Config:
        from_attributes = True


class UserUpdateModel(BaseModel):
    id: int
    username: str | None = None
    password: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None
