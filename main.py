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
    return (Sd)


@app.get("/get-teacher/{teacher_id}")
def get_teacher(teacher_id: int = Path(None, description="l\'index de l\'enseignant dont vous voulez vérifier")):
    return Td[teacher_id]

@app.get("get-classroom/{salle_id}")
def get_classroom(salle_id: str):
    return Sd[salle_id]

@app.get("/get-by-number")
def get_classNumber(num: str):
    for salle_id in Sd:
        if Sd[salle_id]["Numéro_de_Salle"] == num:
            return Sd[salle_id]
    return {"Data": "Not found"}

