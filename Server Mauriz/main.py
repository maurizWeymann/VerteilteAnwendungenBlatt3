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
from typing import List
from yaml import load
#from user import User 
import json
from mydata import User, PutUser, GetQuestion, Question, PutAnswer, ScoringList, MyUsers 

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Demo Rest",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

user_data = MyUsers()
user_data.add_element(User(name = "cup", password = "xyz123"))

user_data.get_elements()
user_df = {}
data = []
user_df = pd.DataFrame(data, columns = [
    'name',
    'password',
    'score',
    ])


########################################################

names = []

question_df = pd.DataFrame(data, columns = [
    'id',
    'question',
    'answer',
    'options',
    ])


user_df = user_df.append({"name":"mo", "password":"xyz123", "score":0}, ignore_index=True) 
user_df = user_df.append({"name":"mau", "password":"z1", "score":0}, ignore_index=True)
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "What is the first name of Iron Man?",
    "answer" : "Tony",
    "options":["Thomas","Antonio"],
}, ignore_index=True) 
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Who is called the god of lightning in Avengers?",
    "answer" : "Thor",
    "options":["Thorsten","Torben"],
}, ignore_index=True)
print(question_df)


'''
I Nutzer anlegen und speichern ohne Model
'''
'''
@app.put("/api/v1/users/adda")
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

'''
I Nutzer anlegen und speichern 
'''
@app.put("/api/v1/users/add")
async def create_user(user: PutUser, response: Response):
    try:
        if user.name not in list(user_df["name"]):
            user_df.loc[len(user_df)] = [user.name, user.password, 0]
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
async def login_user(user: PutUser, response: Response):
    try:
        if user.name not in list(user_df["name"]):
            response.status_code = status.HTTP_403_FORBIDDEN
            return "bad credentials"
        
        else:
            df = user_df.set_index("name", drop = False)
            if user.password in df.loc[user.name]["password"]:
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
@app.get("/api/v1/questions/{number_of_questions}", response_model=GetQuestion)
async def load_questions(number_of_questions: int, response:Response):
    response.status_code = status.HTTP_200_OK
    return MyUsers.get_questions
    
'''
IV Fragen hochladen und speichern
'''
@app.put("/api/v1/questions/add")
async def create_question(question: Question, response: Response):
    try:
        if question not in list(question_df["question"]):
            question_df.loc[len(question_df)] = [question, answer, options]
            response.status_code = status.HTTP_201_CREATED
            return "new question created"
        else:
            response.status_code = status.HTTP_403_FORBIDDEN
            return "already in place"
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

'''
V Antwort(en) hochladen
'''
@app.put("/api/v1/answer")
async def add_anser(answer: PutAnswer, response: Response):
    pass

'''
VI Punkteliste und Highscore aller Spieler abfragen
'''
#@app.get("/api/v1/users/highscore", response_model = List[Question])
@app.get("/api/v1/users/highscore", response_model=ScoringList)
async def return_highscores(response: Response):
    response.status_code = status.HTTP_200_OK
    return question_df.to_dict()

#user_df.loc[len(user_df),"password"] = [password]

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22224, log_level='debug', reload = True)
