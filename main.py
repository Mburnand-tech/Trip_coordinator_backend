from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],

)

## GET requests
# return root, can be used as a test
@app.get("/")
def read_root():
    return {"Ping":"Pongy"}

# get a group, by a group id which has been shared
@app.get("/tripgroup/{id}")
def get_group_by_id(id):
    return {"msg":"Get trip group"}

## POST requests
# create a new group, in the group database


## UPDATE requests
# Update 


## DELETE requests