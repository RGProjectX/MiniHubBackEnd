from fastapi import FastAPI, Depends, HTTPException
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from starlette.responses import JSONResponse
from db import user_collection
from models.user import User, ShowUser, UpdateUser, Login
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)


def get_db():
    try:
        client = MongoClient("mongodb+srv://rohit:rohit@cluster0.3xmfspx.mongodb.net/?retryWrites=true&w=majority")
        yield client.minihub
    finally:
        client.close()
# use the user model to create a new user
@app.post("/register")
async def register(user: User, db=Depends(get_db)):
        # check if user already exists
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    user_collection.insert_one(user.dict())
    return {"message": "User created successfully"}


@app.post("/login")
async def login(user: Login, db=Depends(get_db)):
    user = user_collection.find_one({"email": user.email, "password": user.password})
    if user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
