from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from pydantic import BaseModel

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class User(BaseModel):
    group_id: str
    username: str

## GET requests
# return root, can be used as a test
@app.get("/")
def read_root():
    return {"Ping":"Pongy"}


@app.get("/groupresults/{group_id}")
def get_group_results(group_id: str):
    return 1


## POST requests
# Add new user to a group already created
# @app.post("/createuser")
# def addUser(body: User):
#     return {"msg": "matts building endpoint to add {body.username} to {body.group_id}"}


## UPDATE requests



## DELETE requests

