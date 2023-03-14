from sqlalchemy import Column, Integer, String
from database import Base

class Boost(Base):
    __tablename__ = 'Storage'
    JobId = Column(Integer, primary_key=True, index=True)
    BlockSize = Column(String(256))
    IOType = Column(String(256))
    Time = Column(Integer)
    IOEngine = Column(String(256))

