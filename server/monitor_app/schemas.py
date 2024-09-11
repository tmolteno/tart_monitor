from datetime import datetime
from pydantic import BaseModel


class StatusBase(BaseModel):
    ts: datetime
    last_seen: datetime | None = None


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class TartBase(BaseModel):
    api_key: str


class TartCreate(TartBase):
    name: str
    lat: float
    lon: float
    alt: float


class Tart(TartBase):
    id: int
    lat: float
    lon: float
    alt: float
    is_active: bool
    statuses: list[Status] = []

    class Config:
        from_attributes = True
