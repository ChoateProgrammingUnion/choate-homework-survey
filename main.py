from typing import Optional

from fastapi import FastAPI
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()
data_fp = 'student_classes_data.json'
with open(data_fp, "r") as read_file:
    data = json.load(read_file)
print(type(data['cbowles22@choate.edu']))


@app.get("/")
def read_root():
    return {"message": "Yo hey wassup try /classes/{email}"}


@app.get("/classes/{email}")
def read_classes(email: str):
    return JSONResponse(content=json.dumps(data[email]))


@app.get("/questions")
def read_questions():
    return {"data": "some data"}
