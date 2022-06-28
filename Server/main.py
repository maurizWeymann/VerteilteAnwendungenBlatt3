# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:25:03 2022

@author: 49177
"""

from cmath import log
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
from user import User 
import json

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Demo Rest",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)
def read_from_file(filename):
    with open(filename, "r") as read_file:
        contain = json.load(read_file)
        #print(contain)
        return contain

'''
I Nutzer anlegen und speichern 
'''
@app.put("/api/v1/users/add", status_code=201)
async def create_user(user_name):
    return

'''
II Nutzer anmelden und Spiel starten 
'''
@app.put("/api/v1/users/login", status_code=200)
async def login_user(user_name):
    return

'''
III Fragen abrufen 
'''
@app.get("/api/v1/questions", status_code=200)
async def load_questions():
    #data = read_from_file("I-PUT-users_add.json")
    return "I-PUT-users_add.json"
'''
IV Fragen hochladen und speichern
'''
@app.put("/api/v1/questions/add", status_code=200)
async def create_question():
    return 



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22222, log_level='debug', reload= True)
