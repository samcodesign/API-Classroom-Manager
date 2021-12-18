from fastapi import FastAPI
from typing import Optional
from data import teachers_data as Td
from data import salles_TD as Sd



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sallesTD_Test")
def sallesTest():
    return Sd


@app.get("/Teachers_data")
def TeachersDataTest():
    return Td
