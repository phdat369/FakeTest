from sqlalchemy import Column, Integer, String
from database import Base

class WorldCup(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    country_name = Column(String(100))
    coach_name = Column(String(100))
    group_name = Column(String(100))
    points = Column(Integer)