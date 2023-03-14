from time import sleep
from fastapi import FastAPI, HTTPException, Body, responses, status
from statistics import mode
from sqlalchemy.orm import Session
import models

def get_clusters(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.Boost).offset(skip).limit(limit).all()


def get_cluster_by_id(session: Session, job_id: int):
    result = session.query(models.Boost).filter(models.Boost.JobId == job_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found with this job id")
    return result

