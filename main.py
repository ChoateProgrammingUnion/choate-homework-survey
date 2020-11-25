from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/questions")
def read_questions():
    return {"classes": "EN300, Arcand"}


@app.get("/admin")
def read_questions():
    return {"data": "some data"}
