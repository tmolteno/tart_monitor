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


@app.post("/tarts/", response_model=schemas.Tart)
def create_tart(tart: schemas.TartCreate, db: Session = Depends(get_db)):
    db_tart = crud.get_tart_by_api_key(db, api_key=tart.api_key)
    if db_tart:
        raise HTTPException(status_code=400, detail="API_key already registered")
    return crud.create_tart(db=db, tart=tart)


@app.get("/tarts/", response_model=list[schemas.Tart])
def read_tarts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tarts = crud.get_tarts(db, skip=skip, limit=limit)
    return tarts


@app.get("/tarts/{tart_id}", response_model=schemas.Tart)
def read_tart(tart_id: int, db: Session = Depends(get_db)):
    db_tart = crud.get_tart(db, tart_id=tart_id)
    if db_tart is None:
        raise HTTPException(status_code=404, detail="Tart not found")
    return db_tart


@app.post("/tarts/{tart_id}/statuses/", response_model=schemas.Status)
def create_status_for_tart(
    tart_id: int, status: schemas.StatusCreate, db: Session = Depends(get_db)
):
    return crud.create_tart_status(db=db, status=status, tart_id=tart_id)


@app.get("/statuses/", response_model=list[schemas.Status])
def read_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    statuses = crud.get_statuses(db, skip=skip, limit=limit)
    return statuses
