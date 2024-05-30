from fastapi import FastAPI
from routes.user import user 
from routes.employee import employee

app = FastAPI()
app.include_router(user, tags=["users"]) #user is name of the router app.include_router(user, prefix="/users", tags=["users"])

app.include_router(employee, tags=["employees"])  #app.include_router(employee, prefix="/employees", tags=["employees"])