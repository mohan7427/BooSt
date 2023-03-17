from typing import List
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body, BackgroundTasks
from database import Base, engine
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import crud, schemas
from database import SessionLocal
from starlette.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/jobs")
def read_all_list(session: Session = Depends(get_session)):
    storage_info = crud.get_jobs(session)
    session.close()
    return storage_info


@app.get("/job_id/{job_id}")
def get_by_id(job_id: int, session: Session = Depends(get_session)):
    storage_info = crud.get_job_by_id(session, job_id)
    return storage_info


@app.get("/job_name/{job_name}")
def get_by_name(job_name: str, session: Session = Depends(get_session)):
    storage_info = crud.get_job_by_name(session, job_name)
    return storage_info


@app.get("/results")
def get_by_results(session: Session = Depends(get_session)):
    storage_info = crud.get_results(session)
    session.close()
    return storage_info


@app.post("/job", status_code=status.HTTP_201_CREATED)
def add_job(jobin: schemas.JobIn, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    storage_info = crud.create_job(session, jobin, background_tasks)
    return storage_info


@app.post("/run", status_code=status.HTTP_201_CREATED)
def run_job(jobin: schemas.RunIn, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    storage_info = crud.run_job(session, jobin, background_tasks)
    return storage_info


@app.delete("/job/{job_name}", status_code=status.HTTP_201_CREATED)
async def del_job(job_name: str, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    storage_info = crud.delete_job(session, job_name, background_tasks)
    return storage_info
