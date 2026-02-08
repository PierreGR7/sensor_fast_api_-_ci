from datetime import date

from fastapi import FastAPI
from fastapi.responses import JSONResponse

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sensor_data_app import create_app

store_dict = create_app()
app = FastAPI()

@app.get("/")
def visit(
    store_name:str, year:int, month:int, day:int, sensor_id:int | None = None) -> JSONResponse:

    if not(store_name in store_dict.keys()):
        return JSONResponse(status_code=404, content="Store not found. Search for 'Strasbourg', 'Paris', 'Vasteras', 'Munich', 'Milan'")
    
    if sensor_id and (sensor_id > 7 or sensor_id <0):
        return JSONResponse(status_code=404, content="Sensor_id should be between 0 and 7"
        )
    
    if year < 2019:
        return JSONResponse(status_code=404, content="No data before 2019")

    try:
        date(year, month, day)
    except TypeError:
        return JSONResponse(status_code=404, content="Enter a valid date like '2026-2-2'")

    if date.today() < date(year, month, day):
        return JSONResponse(status_code=404, content="Choose a date in the past")

    if sensor_id is None:
        visit_counts = store_dict[store_name].get_traffic_by_store(date(year, month, day))
    else:
        visit_counts = store_dict[store_name].get_traffic_by_sensor(
            sensor_id, date(year, month, day)
        )

    if visit_counts <0:
        return JSONResponse(status_code=404, content="The store was closed (sunday) try another date")

    return JSONResponse(status_code=200, content=visit_counts)

    # How to run :
    # uvicorn app:app --reload
    # http://127.0.0.1:8000/?store_name=Strasbourg&year=2026&month=2&day=5&sensor_id=0

    