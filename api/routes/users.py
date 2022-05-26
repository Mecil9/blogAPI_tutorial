'''
Author: Mecil Meng
Date: 2022-05-24 21:42:59
LastEditors: Mecil Meng
LastEditTime: 2022-05-25 00:02:13
FilePath: /blogAPI/api/routes/users.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from ..schemas import User, db, UserResponse
from ..utils import get_password_hash, verify_password
import secrets
from ..send_mail import send_registration_mail

router = APIRouter(tags=["User Routes"])


@router.post("/registration",
             response_description="Register a user",
             response_model=UserResponse)
async def registration(user_info: User):
    user_info = jsonable_encoder(user_info)

    # check for duplication
    username_found = await db["users"].find_one({"name": user_info["name"]})
    email_found = await db["users"].find_one({"email": user_info["email"]})

    if username_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Username already exists")

    if email_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Email already exists")

    # hash user password
    user_info["password"] = get_password_hash(user_info["password"])
    # create apikey
    user_info["apiKey"] = secrets.token_hex(30)

    new_user = await db["users"].insert_one(user_info)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})

    # send email
    await send_registration_mail(
        subject="Welcome to JCBEL Blog",
        email_to=user_info['email'],
        body={
            "title": 'Registration Successful',
            "name": user_info['name']
        },
    )

    return created_user
