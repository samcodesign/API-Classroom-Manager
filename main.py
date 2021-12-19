from fastapi import FastAPI, Path
from typing import Optional
import json
from salles import sallesTD


with open("json/teachers_test.json", 'r') as read_file:
    teachers_data = json.load(read_file)
#with open("json/salles.json", 'r') as read_file:
#   sallesTD = json.load(read_file)

description = 'Ceci est prototype D\'API qui concerne la gestion ainsi que la réservation d\'une ou plusieurs salles td de l\'Université des sciences et technologies Houari Boumedienne'




app = FastAPI()


@app.get("/")
def index():
    return description


@app.get("/testing_data")
def TestingData():
    return (sallesTD)


@app.get("/get-teacher/{teacher_id}")
def get_teacher(teacher_id: int = Path(None, description="l\'index de l\'enseignant dont vous voulez vérifier")):
    return teachers_data[teacher_id]


@app.get("/get-salle/{sallesTD_id}")
def get_classroom(sallesTD_id: int = Path(None, description="l\'index de la salle dont vous voulez vérifier")):
    return sallesTD[sallesTD_id]


@app.get("/get-by-number")
def get_classNumber(num: int):
    for sallesTD_id in sallesTD:
        if sallesTD[sallesTD_id]["number"] == num:
            return sallesTD[sallesTD_id]
    return {"Data": "Not found"}
