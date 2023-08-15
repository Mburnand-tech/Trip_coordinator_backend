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


async def fetch_group_exists(group_id):
    #return {"matty": "answer"}
    document = await groupCollection.find_one({"group_name": group_id})
    if document:
        return True
    else:
        return False
    

async def create_new_group(group_id):
    #"group_members": ["jimmy"]
    ## Notes for tomorrow, I think it has a problem with the datatype I'm giving it....
    document = await groupCollection.insert_one({"group_name": "fraserBGroup"})
    return document

# if __name__ == "__main__":
#     result = asyncio.run(create_document())
#     print("Inserted document ID:", result)