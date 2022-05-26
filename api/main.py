'''
Author: Mecil Meng
Date: 2022-05-24 21:37:36
LastEditors: Mecil Meng
LastEditTime: 2022-05-25 14:15:34
FilePath: /blogAPI/api/main.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''

from fastapi import FastAPI

from .routes import auth, blog_content, password_reset, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(password_reset.router)
app.include_router(blog_content.router)
