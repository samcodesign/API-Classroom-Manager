from fastapi import FastAPI, Path
from typing import Optional
import json
from salles import sallesTD
from teachers_data import teachers_data
from pydantic import BaseModel


# with open("json/teachers_test.json", 'r') as read_file:
#    teachers_data = json.load(read_file)
# with open("json/salles.json", 'r') as read_file:
#   sallesTD = json.load(read_file)
description = 'Ceci est prototype D\'API qui concerne la gestion ainsi que la réservation d\'une ou plusieurs salles td de l\'Université des sciences et technologies Houari Boumedienne'

class Teacher(BaseModel):
    First_name : str
    Last_name: str
    Password: str
    email: str

class UpdateTeacher(BaseModel):
    First_name: Optional[str] = None
    Last_name: Optional[str] = None
    Password: Optional[str] = None
    email: Optional[str] =  None

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


@app.get("/get-by-name")
def getName(*, name: Optional[str] = None, test: int):
    for teacher_id in teachers_data:
        if teachers_data[teacher_id]["Last_name"] == name:
            return teachers_data[teacher_id]
    return {"Data": "Not Found"}

@app.post("/create-teacher/{teacher_id}")
def CreateTeacher(teacher_id:int, teacher: Teacher):
    if teacher_id in teachers_data:
        return {"Error": "Teacher already exist in database"}
    
    teachers_data[teacher_id] = teacher
    return teachers_data[teacher_id]


@app.put("/update-teacher/{teacher_id}")
def updateTeacher(teacher_id : int, teacher: UpdateTeacher):
    if teacher_id in teachers_data:
        return {"Error": "Teacher does not exist in database"}
    
    teachers_data[teacher_id] = teacher
    return teachers_data[teacher_id]
