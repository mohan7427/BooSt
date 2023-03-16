from time import sleep
from fastapi import FastAPI, HTTPException, Body, responses, status
from statistics import mode
from sqlalchemy.orm import Session
import models, schemas

import os
import subprocess as sp
from subprocess import call
from subprocess import Popen, PIPE

def get_jobs(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.Boost).offset(skip).limit(limit).all()


def get_job_by_id(session: Session, job_id: int):
    result = session.query(models.Boost).filter(models.Boost.JobId == job_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found with this job id")
    return result


def get_job_by_name(session: Session, job_name: str):
    result = session.query(models.Boost).filter(models.Boost.JobName == job_name).first()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found with this job name")
    return result


def create_job(session: Session, jobin: schemas.JobIn, background_tasks):
    result = session.query(models.Boost).filter(models.Boost.JobName == jobin.job_name).first()

    if result:
        raise HTTPException(status_code=404, detail="Already exists the same job name")

    session_job = models.Boost(BlockSize=jobin.block_size, IODepth=jobin.io_depth, RunTime=jobin.run_time, IOEngine=jobin.io_engine, JobName=jobin.job_name, DiskName=jobin.disk_name, NumJobs=jobin.num_jobs, ReadWrite=jobin.read_write)
    session.add(session_job)
    session.commit()
    session.close()

    return "Noted you jobId"


def run_job(session: Session, jobin: schemas.RunIn, background_tasks):
    os.system("python3 backend_script.py {} {} {} {} {}".format(jobin.IODepth, jobin.NumJobs, jobin.ReadWrite, jobin.BlockSize, jobin.RunTime))
#    command = "python3 backend_script.py jobin.IODepth jobin.NumJobs jobin.ReadWrite jobin.BlockSize jobin.RunTime"
    return "Noted you jobId"


def delete_job(session: Session, job_name: str, background_tasks):
    result = session.query(models.Boost).filter(models.Boost.JobName == job_name).first()

    if not result:
        raise HTTPException(status_code=404, detail="Data with this job name is not present")

    session.delete(result)
    session.commit()
    session.close()


