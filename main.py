from fastapi import FastAPI
from typing import Optional
from data import teachers_data as Td
from data import salles_TD as Sd
from data import description


app = FastAPI()


@app.get("/")
def index():
    return description


@app.get("/testing_data")
def TestingData():
    return Td + ' ' + Sd

