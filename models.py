# module imports
import enum
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

# create and initialize the db engine
engine = create_engine('sqlite:///db.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class SensorType(enum.Enum):
    """
    The Sensor Type enumeration
    """
    TEMPERATURE = 0
    PRESSURE = 1
    MOISTURE = 2
    UPTIME = 3
    OXYGEN_LVL = 4


class MachOPData(Base):
    """
    MachOP Data Model
    """
    __tablename__ = 'machop_data'
    id = Column(Integer, primary_key=True)
    mac_op_id = Column(Integer)
    timestamp = Column(DateTime)
    sensor_type = Column(Enum(SensorType))
    value = Column(Float)
