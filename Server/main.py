# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:25:03 2022

@author: 49177
"""

from cmath import log
from distutils.log import error
from hashlib import new
from imp import reload
from pickletools import read_uint1
from fastapi import FastAPI, status, Response
import os
import pandas as pd
#from models import User
#from models import Questions
#import logic
import uvicorn
import random
import time

from yaml import load
#from user import User 
import json

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Demo Rest",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

data = []
names = []
user_df = {}

user_df = pd.DataFrame(data, columns = [
    'user_name',
    'password',
    'score',
    ])


user_df = user_df.append({"user_name":"mo", "password":"xyz123", "score":0}, ignore_index=True) 

'''
I Nutzer anlegen und speichern 
'''
@app.put("/api/v1/users/add")
async def create_user(user_name: str, password: str, response: Response):
    try:
        if user_name not in list(user_df["user_name"]):
            user_df.loc[len(user_df)] = [user_name, password, 0]
            response.status_code = status.HTTP_201_CREATED
            return "new user created"
        else:
            response.status_code = status.HTTP_403_FORBIDDEN
            print(user_df)
            return "user already in use"
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    
'''
II Nutzer anmelden und Spiel starten 
'''
@app.put("/api/v1/users/login")
async def login_user(user_name: str, password: str, response: Response):
    try:
        if user_name not in list(user_df["user_name"]):
            response.status_code = status.HTTP_403_FORBIDDEN
            return "bad credentials"
        
        else:
            df = user_df.set_index("user_name", drop = False)
            if password in df.loc[user_name]["password"]:
                response.status_code = status.HTTP_202_ACCEPTED
                return "successful logged in "
            else:
                response.status_code = status.HTTP_401_UNAUTHORIZED
                return "wrong combination"
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


'''
III Fragen abrufen 
'''
@app.get("/api/v1/questions")
async def load_questions(response:Response):
    response.status_code = status.HTTP_200_OK
    return user_df.to_dict()
    
'''
IV Fragen hochladen und speichern
'''
@app.put("/api/v1/questions/add", status_code=200)
async def create_question():
    return 

#user_df.loc[len(user_df),"password"] = [password]

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22224, log_level='debug', reload = True)
