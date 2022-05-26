'''
Author: Mecil Meng
Date: 2022-05-24 21:57:31
LastEditors: Mecil Meng
LastEditTime: 2022-05-25 14:04:28
FilePath: /blogAPI/api/schemas.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
import os

import motor.motor_asyncio
from bson import ObjectId
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, Field

# Load Env
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client.blog_api


# BSON and JSON
class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"{v} is not a valid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Mecil Meng",
                "email": "mecil9@jcble.com",
                "password": "123456",
            }
        }


class UserResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Mecil Meng",
                "email": "mecil9@jcble.com",
            }
        }


class BlogContent(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Blog title",
                "body": "Blog content",
            }
        }


class BlogContentResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)
    author_name: str = Field(...)
    author_id: str = Field(...)
    create_at: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Blog title",
                "body": "Blog content",
                "author_name": "name of the author",
                "author_id": "ID of the author",
                "created_at": "date create"
            }
        }


class TokenData(BaseModel):
    id: str


class PassswordReset(BaseModel):
    email: EmailStr


class NewPassword(BaseModel):
    password: str
