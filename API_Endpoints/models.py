from sqlalchemy import Column, Integer, String
from database import Base

class Boost(Base):
    __tablename__ = 'Storage'
    JobId = Column(Integer, primary_key=True, index=True)
    BlockSize = Column(String(256))
    IODepth= Column(String(256))
    RunTime = Column(String(256))
    IOEngine = Column(String(256))
    JobName = Column(String(256))
    DiskName = Column(String(256))
    NumJobs = Column(Integer)
    ReadWrite = Column(String(256))
