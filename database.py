# This is a class structure I can define in model
#from model import Todo
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
database = client.TripCoordinator
groupCollection = database.groups
usersCollection = database.users

async def fetch_group_results(group_id):
    document = await groupCollection.find_one({"group_name": group_id})
    return document