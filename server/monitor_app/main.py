from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tarts/", response_model=schemas.User)
def create_tart(tart: schemas.UserCreate, db: Session = Depends(get_db)):
    db_tart = crud.get_tart_by_email(db, email=tart.email)
    if db_tart:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_tart(db=db, tart=tart)


@app.get("/tarts/", response_model=list[schemas.User])
def read_tarts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tarts = crud.get_tarts(db, skip=skip, limit=limit)
    return tarts


@app.get("/tarts/{tart_id}", response_model=schemas.User)
def read_tart(tart_id: int, db: Session = Depends(get_db)):
    db_tart = crud.get_tart(db, tart_id=tart_id)
    if db_tart is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_tart


@app.post("/tarts/{tart_id}/statuses/", response_model=schemas.Item)
def create_status_for_tart(
    tart_id: int, status: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_tart_status(db=db, status=status, tart_id=tart_id)


@app.get("/statuses/", response_model=list[schemas.Item])
def read_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    statuses = crud.get_statuses(db, skip=skip, limit=limit)
    return statuses
