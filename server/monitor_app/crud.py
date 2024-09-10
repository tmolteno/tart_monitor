from sqlalchemy.orm import Session

from . import models, schemas


def get_tart(db: Session, tart_id: int):
    return db.query(models.Tart).filter(models.Tart.id == tart_id).first()


def get_tart_by_email(db: Session, email: str):
    return db.query(models.Tart).filter(models.Tart.email == email).first()


def get_tarts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tart).offset(skip).limit(limit).all()


def create_tart(db: Session, tart: schemas.TartCreate):
    fake_hashed_password = tart.password + "notreallyhashed"
    db_tart = models.Tart(email=tart.email, hashed_password=fake_hashed_password)
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
