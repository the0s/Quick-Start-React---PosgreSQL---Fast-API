# build a schema using pydantic
from pydantic import BaseModel
from typing import Union


class Result(BaseModel):
    year: int
    city: str
    sport: str
    discipline: str
    athlete: str
    gender: str
    event: str
    medal: str
    country_code: Union[str, None] = None

    class Config:
        orm_mode = True


class Country(BaseModel):
    name: str
    code: str
    population: Union[int, None] = None
    gdp: Union[float, None] = None

    class Config:
        orm_mode = True


class CountryMedal(BaseModel):
    code: str = ""
    country: str = "N/A"
    gold: int = 0
    silver: int = 0
    bronze: int = 0
