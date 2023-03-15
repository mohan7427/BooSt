from ipaddress import ip_address
from pydantic import BaseModel
from typing import Optional, List, Union
from enum import Enum
from database import Base

class JobIn(BaseModel):
    block_size: str
    io_depth: str
    run_time: str
    io_engine: str
    job_name: str
    disk_name: str
    num_jobs: int
    read_write: str

    class Config:
        orm_mode = True
