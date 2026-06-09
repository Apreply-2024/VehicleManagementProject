from sqlalchemy import Column, Integer, String

from database.database import Base


class VehicleModel(Base):

    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    vin = Column(String, unique=True)
    status = Column(String)