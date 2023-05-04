from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    name: str
    email: str
    description: str
    languages: list
    url: str
    class Config:
        schema_extra = {
            "example": {
                "name": "Project Name",
                "email": "johndoe@gmail.com",
                "description": "Project Description",
                "languages": ["Python", "FastAPI"],
                "url": "http://yourfile.zip"
            }
        }


