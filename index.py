from fastapi import FastAPI
from routes.user import user

app = FastAPI()
app.include_router(user) #user is name of the router