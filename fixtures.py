# module import
import datetime
from models import MachOPData, SensorType, engine, Base, db_session

Base.metadata.create_all(bind=engine)


def create_fixtures():
    """
    This test fixture is to demonstrate the datamodel for storing the sensor data
    """
    entry1 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.TEMPERATURE, value=34.5)
    entry2 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.PRESSURE, value=144.7)
    entry3 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.MOISTURE, value=14.5)
    entry4 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.OXYGEN_LVL, value=99.7)

    entry5 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.TEMPERATURE, value=34.5)
    entry6 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.PRESSURE, value=144.7)
    entry7 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.MOISTURE, value=14.5)
    entry8 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=32, second=12),
                        sensor_type=SensorType.OXYGEN_LVL, value=99.7)

    entry9 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.TEMPERATURE, value=34.5)
    entry10 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.PRESSURE, value=144.7)
    entry11 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.MOISTURE, value=14.5)
    entry12 = MachOPData(mac_op_id=1, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.OXYGEN_LVL, value=99.7)

    entry13 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.TEMPERATURE, value=34.5)
    entry14 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.PRESSURE, value=144.7)
    entry15 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.MOISTURE, value=14.5)
    entry16 = MachOPData(mac_op_id=2, timestamp=datetime.datetime(year=2022, day=19, month=6,
                                                                 hour=14, minute=33, second=12),
                        sensor_type=SensorType.OXYGEN_LVL, value=99.7)

    db_session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10,
                        entry11, entry12, entry13, entry14, entry15, entry16])
    db_session.commit()
