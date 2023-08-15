from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from database import (
    fetch_group_results,
    fetch_group_exists,
    create_new_group,
)

from model import (
    User
)

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


# @app.get("/groupresults/{group_id}")
# async def get_group_results(group_id: str):
#     response = await fetch_group_results()
#     if response:
#         return response
#     raise HTTPException(404)

@app.get("/group/{group_id}")
async def get_group_exists(group_id: str):
    response = await fetch_group_exists(group_id)
    #return {"mat": "b"}
    if response:
        return response
    raise HTTPException(404)

## POST requests
# Add new user to a group already created
# @app.post("/createuser")
# def addUser(body: User):
#     return {"msg": "matts building endpoint to add {body.username} to {body.group_id}"}

@app.post("/creategroup", response_model=User)
async def post_new_group(group_id: User):
    response = await create_new_group(group_id.dict())
    if response:
        return response
    raise HTTPException(400, f"group id doesn't exist from MATT")

## UPDATE requests



## DELETE requests

