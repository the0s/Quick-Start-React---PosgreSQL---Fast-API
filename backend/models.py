from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    city = Column(String)
    sport = Column(String)
    discipline = Column(String)
    athlete = Column(String)
    gender = Column(String)
    event = Column(String)
    medal = Column(String)
    country_code = Column(String)


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    code = Column(String)
    population = Column(Integer)
    gdp = Column(Float)
