from sqlalchemy.orm import Session

from . import models, schemas


def get_tart(db: Session, tart_id: int):
    return db.query(models.Tart).filter(models.Tart.id == tart_id).first()


def get_tart_by_api_key(db: Session, api_key: str):
    return db.query(models.Tart).filter(models.Tart.api_key == api_key).first()


def get_tarts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tart).offset(skip).limit(limit).all()


def create_tart(db: Session, tart: schemas.TartCreate):
    db_tart = models.Tart(api_key=tart.api_key, name=tart.name, lat=tart.lat, lon=tart.lon, alt=tart.alt)
    db.add(db_tart)
    db.commit()
    db.refresh(db_tart)
    return db_tart


def get_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()


def create_tart_status(db: Session, status: schemas.StatusCreate, tart_id: int):
    db_status = models.Status(**status.dict(), owner_id=tart_id)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status
