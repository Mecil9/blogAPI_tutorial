'''
Author: Mecil Meng
Date: 2022-05-24 23:19:08
LastEditors: Mecil Meng
LastEditTime: 2022-05-25 12:29:51
FilePath: /blogAPI/api/send_mail.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from typing import Dict

load_dotenv()


class Envs:
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM = os.getenv("MAIL_FROM")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")


conf = ConnectionConfig(MAIL_USERNAME=Envs.MAIL_USERNAME,
                        MAIL_PASSWORD=Envs.MAIL_PASSWORD,
                        MAIL_FROM=Envs.MAIL_FROM,
                        MAIL_PORT=Envs.MAIL_PORT,
                        MAIL_SERVER=Envs.MAIL_SERVER,
                        MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
                        MAIL_TLS=False,
                        MAIL_SSL=True,
                        USE_CREDENTIALS=True,
                        TEMPLATE_FOLDER="api/templates")


async def send_registration_mail(subject: str, email_to: str, body: dict):
    message = MessageSchema(subject=subject,
                            recipients=[email_to],
                            template_body=body,
                            subtype="html")
    fm = FastMail(conf)
    await fm.send_message(message=message, template_name="email.html")


async def password_reset(subject: str, email_to: str, body: Dict):
    message = MessageSchema(subject=subject,
                            recipients=[email_to],
                            template_body=body,
                            subtype="html")
    fm = FastMail(conf)
    await fm.send_message(message, template_name="Password_reset.html")
