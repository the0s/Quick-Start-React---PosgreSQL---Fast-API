import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from schema import Result as SchemaResult
from schema import Country as SchemaCountry
from schema import CountryMedal
from typing import List
from models import Result as ModelResult
from models import Country as ModelCountry
import csv
import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get('/populate/')
async def result():
    db.session.query(ModelCountry).delete()
    db.session.query(ModelResult).delete()
    db.session.commit()

    cur_path = os.path.dirname(__file__)
    filename = os.path.join(cur_path, "raw-data/dictionary.csv")
    with open(filename, mode='r') as inFile:
        csv_reader = csv.DictReader(inFile)
        for row in csv_reader:
            gpd = row.get('GDP per Capita')
            gpd = gpd if gpd else None
            population = row.get('Population')
            population = population if population else None
            db_result = ModelCountry(code=row.get('Code'),
                                     name=row.get('Country'),
                                     population=population,
                                     gdp=gpd,
                                     )
            db.session.add(db_result)
        db.session.commit()

    #
    cur_path = os.path.dirname(__file__)
    filename = os.path.join(cur_path, "raw-data/2004-2012.csv")
    with open(filename, mode='r') as inFile:
        csv_reader = csv.DictReader(inFile)
        for row in csv_reader:
            db_result = ModelResult(year=row.get('Year'),
                                    city=row.get('City'),
                                    sport=row.get('Sport'),
                                    discipline=row.get('Discipline'),
                                    athlete=row.get('Athlete'),
                                    event=row.get('Event'),
                                    medal=row.get('Medal'),
                                    gender=row.get('Gender'),
                                    country_code=row.get('Country')
                                    )
            db.session.add(db_result)
        db.session.commit()
    return {"message": "done"}


@app.get('/results/', response_model=List[SchemaResult])
async def result():
    result = db.session.query(ModelResult).all()
    return result


@app.get('/countries/', response_model=List[SchemaCountry])
async def country():
    country = db.session.query(ModelCountry).all()
    return country


@app.get('/medals/{year}', response_model=List[CountryMedal])
@app.get('/medals/', response_model=List[CountryMedal])
async def medals(year: int = None):
    if year is not None:
        user_counts = db.session.query(
            ModelResult.medal,
            ModelResult.country_code,
            func.count(ModelResult.medal).label("total_counts")
        ).filter(
            ModelResult.year == year
        ).group_by(
            ModelResult.medal,  ModelResult.country_code,
        ).all()
    else:
        user_counts = db.session.query(
            ModelResult.medal,
            ModelResult.country_code,
            func.count(ModelResult.medal).label("total_counts")
        ).group_by(
            ModelResult.medal,  ModelResult.country_code,
        ).all()

    collect = {}

    country = db.session.query(ModelCountry).all()
    mapping = {c.code: c.name for c in country}
    for k in user_counts:
        if k.country_code:
            collect.setdefault(k.country_code, {})
            collect[k.country_code][k.medal.lower()] = k.total_counts
    #
    c_list = []
    for k, v in collect.items():
        v['code'] = k
        v['country'] = name = mapping.get(k, k)
        c_list.append(v)
    return c_list


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
