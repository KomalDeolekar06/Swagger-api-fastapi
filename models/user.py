from pydantic import BaseModel

class User(BaseModel):
    name : str
    email : str
    password : str
    
class Employee(BaseModel):
    name : str
    surname :str
    salary : int
    department : str

