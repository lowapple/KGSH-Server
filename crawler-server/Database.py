from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

async def insert_meal(dict):
    db = client.kgsh
    collection = db['meals']
    cursor = collection.find(dict).count()
    if cursor == 0:
        collection.insert(dict)

async def create_meal_choice_id(meal_id):
    db = client.kgsh
    collection = db['meal_choices']
    cursor = collection.find({
        "meal_id" : meal_id
    }).count()
    if cursor == 0:
        result = collection.insert_one({
            "meal_id" : meal_id,
            "good" : 0,
            "bad" : 0
        }).inserted_id
        return result
    else:
        return collection.find_one({
            "meal_id" : meal_id
        })['_id']