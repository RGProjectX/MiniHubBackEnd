import json
from fastapi import FastAPI, Depends, HTTPException
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from starlette.responses import JSONResponse
from db import user_collection, project_collection
from models.user import User, ShowUser, Login, UpdateUser
from models.project import Project
from bson import json_util

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
        raise HTTPException(status_code=400, detail="Email ID is already registered.")

    user_collection.insert_one(user.dict())
    return {"message": "User created successfully"}


@app.post("/login")
async def login(user: Login, db=Depends(get_db)):
    user = user_collection.find_one({"email": user.email, "password": user.password})
    if user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    

# update user details
@app.post("/users/update")
async def update(user: UpdateUser, db=Depends(get_db)):
    # print(user.email)
    current_user = user_collection.find_one({"email": user.email})
    if current_user:
        update_user = {}
        if user.firstName:
            update_user["firstName"] = user.firstName
        if user.lastName:
            update_user["lastName"] = user.lastName
        if user.college:
            update_user["college"] = user.college
        if user.email:
            update_user["email"] = user.email
        user_collection.update_one({"email": user.email}, {"$set": update_user})
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
#  www.rohit.com/user/sakshi@gmail.com

@app.get("/user/{email}",response_model=ShowUser)
async def get_user(email: str, db=Depends(get_db)):
    user = user_collection.find_one({"email": email})
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

# user_collection - User Details
# project_collection = Project Details

@app.post("/upload")
async def upload(project: Project, db=Depends(get_db)):
    project_collection.insert_one(project.dict())
    return {"message": "Project uploaded successfully"}

@app.get("/projects")
async def get_projects(db=Depends(get_db)):
    projects = list(project_collection.find())
    # print(projects)
    return json.loads(json_util.dumps(projects))

# ww.rohit.com.project/MiniHUb
@app.get("/project/{name}")
async def get_project(name: str, db=Depends(get_db)):
    projects =project_collection.find_one({"name": name})
    return json.loads(json_util.dumps(projects))
