# create a user model

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    college: str
    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@gmail.com",   
                "password": "password",
                "college": "IIT Bombay"
            }
        }

class ShowUser(BaseModel):
    firstName: str
    lastName: str
    email: str
    college: str
    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@gmail.com",
                "college": "IIT Bombay"
            }
        }

class UpdateUser(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    college: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "firstName": "John",
                "lastName": "Doe",
                "email": "johndoe@gmail.com",
                "college": "IIT Bombay"
            }
        }

class Login(BaseModel):
    email: str
    password: str
    class Config:
        schema_extra = {
            "example": {
                "email": "johndoe@gmail.com",
                "password": "password"
            }
        }
        
