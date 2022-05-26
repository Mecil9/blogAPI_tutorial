'''
Author: Mecil Meng
Date: 2022-05-24 23:00:19
LastEditors: Mecil Meng
LastEditTime: 2022-05-24 23:05:36
FilePath: /blogAPI/api/utils.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
