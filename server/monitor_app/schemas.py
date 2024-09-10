from pydantic import BaseModel


class StatusBase(BaseModel):
    title: str
    description: str | None = None


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class TartBase(BaseModel):
    email: str


class TartCreate(TartBase):
    password: str


class Tart(TartBase):
    id: int
    is_active: bool
    items: list[Status] = []

    class Config:
        orm_mode = True
