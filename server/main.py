import sqlite3

from typing import Union
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel


con = sqlite3.connect("tart_monitor.db")

app = FastAPI()

class Tart(BaseModel):
    name: str
    lat: float
    lon: float
    last_ping: datetime
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    '''
        The comment goes here.
    '''
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, tart: Tart):
    return {"item_name": tart.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
