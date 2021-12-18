import json


with open("data/teachers_test.json", 'r') as read_file:
    teachers_data = json.load(read_file)

with open("json/salles.json", 'r') as read_file:
    salles_TD = json.load(read_file)



description = 'Ceci est prototype D\'API qui concerne la gestion ainsi que la réservation d\'une ou plusieurs salles td de l\'Université des sciences et technologies Houari Boumedienne'