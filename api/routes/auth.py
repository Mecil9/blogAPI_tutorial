'''
Author: Mecil Meng
Date: 2022-05-25 00:44:00
LastEditors: Mecil Meng
LastEditTime: 2022-05-25 13:58:52
FilePath: /blogAPI/api/routes/auth.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .. import utils
from ..oath2 import create_access_token
from ..schemas import db

router = APIRouter(prefix='/login', tags=['Authentication'])


@router.post("", status_code=status.HTTP_200_OK)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    """
  Log in a user.
  """
    user = await db["users"].find_one({"name": user_credentials.username})

    if user and utils.verify_password(user_credentials.password,
                                      user["password"]):
        access_token = create_access_token({"id": user["_id"]})

        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Invalide user credentials')
