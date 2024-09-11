from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base


class Tart(Base):
    __tablename__ = "tarts"

    id = Column(Integer, primary_key=True)
    api_key = Column(String, unique=True, index=True)
    name = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    alt = Column(Float)
    is_active = Column(Boolean, default=True)

    statuses = relationship("Status", back_populates="owner")

class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime)
    last_seen = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("tarts.id"))

    owner = relationship("Tart", back_populates="statuses")
