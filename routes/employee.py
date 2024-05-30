from fastapi import APIRouter
from models.user import Employee
from config.db import db
from schemas.user import serializeList , serializeDict
from bson import ObjectId

employee = APIRouter()

#routes
@employee.get('/employees')
async def find_all_users():
    print(db.employee.find())
    print(serializeList(db.employee.find()))
    return serializeList(db.employee.find())

@employee.get('/employees/{id}')
async def find_one_user(id):
    return serializeDict(db.employee.find_one({"_id":ObjectId(id)}))

@employee.post('/employees')
async def create_user(employee : Employee):  #user of type User which we have created on Models so it can accept only that parameters name email password
    db.employee.insert_one(dict(employee))
    
    return serializeList(db.employee.find())

@employee.put('/employees/{id}')
async def update_user(id , employee: Employee):  
    db.employee.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(employee)}) #we used objectId because mongodb understands this only
    #if we directly return this it will give us previous state so we returning it with findone after updating

    return serializeDict(db.employee.find_one({"_id": ObjectId(id)}))

@employee.delete('/employees/{id}')
async def delete_user(id):  

    return serializeDict(db.employee.find_one_and_delete({"_id": ObjectId(id)}))