from os import SF_SYNC
from fastapi import FastAPI, Path
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
    return (Td + Sd)


@app.get("/get-teacher/{teacher_id}")
def get_teacher(teacher_id: int = Path(None, description="l\'index de l\'enseignant dont vous voulez vérifier")):
    return Td[teacher_id]

@app.get("get-classrooms/{classrooms_id}")
def get_classroom(classrooms_id: int):
    return Sd[classrooms_id]

@app.get("/get-by-number")
def get_classNumber(Numéro_de_salle: int):
    for classrooms_id in Sd:
        if Sd[classrooms_id]["Numéro de salle"] == Numéro_de_salle
            return Sd[classrooms_id]
    return {"Data": "Not found"}
