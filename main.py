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


## POST requests
# Add new user to a group already created
@app.post("/createuser")
def addUser(group_id, username):
    return {"msg": "matts building endpoint to add {username} to {group_id}"}


## UPDATE requests



## DELETE requests

