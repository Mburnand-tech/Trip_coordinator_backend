# This is a class structure I can define in model
#from model import Todo
import motor.motor_asyncio
from model import User

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
database = client.TripCoordinator
groupCollection = database.groups
usersCollection = database.users

async def fetch_group_results(group_id):
    document = await groupCollection.find_one({"group_name": group_id})
    return document


async def fetch_group_exists(group_id):
    #return {"matty": "answer"}
    document = await groupCollection.find_one({"group_name": group_id})
    if document:
        return True
    else:
        return False
    

async def create_new_group(group_id):
    document = group_id
    result = await groupCollection.insert_one(document)
    return document