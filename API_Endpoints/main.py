from typing import List
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body
from database import Base, engine
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import crud
from database import SessionLocal

Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/get_all")
def read_all_list(session: Session = Depends(get_session)):
    storage_list = crud.get_clusters(session)
    session.close()
    return storage_list


@app.get("/job_id/{job_id}")
def get_by_id(job_id: int, session: Session = Depends(get_session)):
    storage_info = crud.get_cluster_by_id(session, job_id)
    return storage_info
