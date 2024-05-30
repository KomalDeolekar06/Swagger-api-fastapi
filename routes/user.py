from fastapi import APIRouter
from models.user import User
from config.db import db
from schemas.user import userEntity , usersEntity
from bson import ObjectId

user = APIRouter()

#routes
@user.get('/users')
async def find_all_users():
    print(db.user.find())
    print(usersEntity(db.user.find()))
    return usersEntity(db.user.find())

@user.get('/users/{id}')
async def find_one_user(id):
    return userEntity(db.user.find_one({"_id":ObjectId(id)}))

@user.post('/users')
async def create_user(user: User):  #user of type User which we have created on Models so it can accept only that parameters name email password
    db.user.insert_one(dict(user))
    
    return usersEntity(db.user.find())

@user.put('/users/{id}')
async def update_user(id , user: User):  
    db.user.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(user)}) #we used objectId because mongodb understands this only
    #if we directly return this it will give us previous state so we returning it with findone after updating

    return userEntity(db.user.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}')
async def delete_user(id):  

    return userEntity(db.user.find_one_and_delete({"_id": ObjectId(id)}))


