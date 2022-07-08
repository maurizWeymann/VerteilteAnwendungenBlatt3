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
from fastapi import FastAPI, status, Response, Path
import pandas as pd
import uvicorn
import random
import time
from typing import List
from yaml import load
import json
from mydata import User, PutUser, Question, PutQuestion, PutAnswer, ScoringList, MyUsers 

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Demo Rest",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

user_data = MyUsers()

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
question_list = []
scoring_list = []

question_df = pd.DataFrame(data, columns = [
    'id',
    'question',
    'answer',
    'options',
    ])


user_df = user_df.append({"name":"mo", "password":"xyz123", "score":0}, ignore_index=True) 
user_df = user_df.append({"name":"mau", "password":"z1", "score":0}, ignore_index=True)
#############################################
question_list.append({
    "question_id": 1,
    "question" : "What is the first name of Iron Man?",
    #"answer" : "Tony",
    "options":["Thomas","Antonio"],
}) 
#############################################
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Who is called the god of lightning in Avengers?",
    "answer" : "Thor",
    "options":["Thorsten","Torben"],
}, ignore_index=True)
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Who carries a shield of American flag theme in Avengers?",
    "options":["Steve", "Roger"],
    "answer" : "Captain America"
}, ignore_index=True)
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "What is the first name of Iron Man?",
    "options":["Thomas","Antonio"],
    "answer" : "Tony"
}, ignore_index=True)
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Which avenger is green in color?",
    "options":["Spiderman","Vision"],
    "answer" : "Hulk"
}, ignore_index=True)
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Which avenger can change it's size?",
    "options":["ChangeMan", "SizeMan"],
    "answer" : "AntMan"
}, ignore_index=True)
question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Which Avenger is red in color and has mind stone?",
    "options":["MindMan","RedMan"],
    "answer" : "Vision"
}, ignore_index=True)

#question_list.append( {"question_id" : question_df.loc[0, "id"], "question" : question_df.loc[0, "question"], "options" : question_df.loc[0, "options"] + [(question_df.loc[0, "answer"])] } )
for index, user in user_df.iterrows() :
    scoring_list.append({ "name" : user_df.loc[index, "name"], "score" : user_df.loc[index, "score"] })


print( question_list.append( {
    "question_id" : question_df.loc[0, "id"],
    "question" : question_df.loc[0, "question"]
    } )
)

def save_questions_to_csv():
    question_df.to_csv('question.csv',index=False)
    
def load_questions_from_csv():
    question_df = pd.read_csv('question.csv')

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
@app.get("/api/v1/questions/{number_of_questions}", response_model = List[Question])
async def load_questions(*,number_of_questions: int = Path(title="The ID of the item to get", ge=1, le=len(question_df)), response:Response):
    response.status_code = status.HTTP_200_OK
    question_list = []
    for sample in random.sample(range(0,len(question_df)),number_of_questions):
        question_list.append( {"question_id" : question_df.loc[sample, "id"], "question" : question_df.loc[sample, "question"], "options" : question_df.loc[sample, "options"] + [(question_df.loc[sample, "answer"])] } )
    return question_list    
'''
IV Fragen hochladen und speichern
'''
@app.put("/api/v1/questions/add")
async def create_question(question: PutQuestion, response: Response):
    try:
        if question.question not in list(question_df["question"]):
            question_df.loc[len(question_df)] = [ max(list(question_df["id"]))+1, question.question, question.answer, question.options]
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
    try:
        scoring_list = []
        for index, user in user_df.iterrows() :
            scoring_list.append({ "name" : user_df.loc[index, "name"], "score" : user_df.loc[index, "score"] })
        response.status_code = status.HTTP_200_OK
        return {"user" : scoring_list}
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22224, log_level='debug', reload = True)
