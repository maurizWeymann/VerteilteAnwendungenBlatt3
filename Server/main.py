# -*- coding: utf-8 -*-
'''
Intalliert alle nowendigen Pakete
    pip install -r requirements.txt
    
Erzeugt requirements.txt
python -m pip freeze > requirements.txt

API Explanation
https://rapidapi.com/apidojo/api/transfermarket

'''

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

import json
import os
from mydata import User, PutUser, Question, PutQuestion, PutAnswer, ScoringList 
from ast import literal_eval

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Demo Rest",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

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
user_id = []

question_df = pd.DataFrame(data, columns = [
    'id',
    'question',
    'answer',
    'options',
    ])


'''
Handle Question Data
'''
def load_questions_from_csv():
    return pd.read_csv('question.csv', delimiter=";",converters={'options': literal_eval})

def save_questions_to_csv(question_df):
    question_df.to_csv('question.csv',index=False, sep=";")
'''
Handle User Data
'''
def load_users_from_csv():
    return pd.read_csv('user.csv')

def save_user_to_csv(user_df):
    user_df.to_csv('user.csv',index=False)


question_df = question_df.append({
    "id":len(question_df)+1,
    "question" : "Who is called the god of lightning in Avengers?",
    "answer" : "Thor",
    "options":["Thorsten","Torben"],
}, ignore_index=True)


'''
I Nutzer anlegen und speichern 
'''
@app.put("/api/v1/users/add")
async def create_user(user: PutUser, response: Response):
    try:
        try:
            user_df = load_users_from_csv()
        except:
            print("unable to load data from csv file") 
        
        if user.name not in list(user_df["name"]):
            user_df.loc[len(user_df)] = [user.name, user.password, 0]
            
            try:
                save_user_to_csv(user_df)
                response.status_code = status.HTTP_201_CREATED
                return "new user created"
            except:
                print("unable to save user data to csv file") 
            
        else:
            response.status_code = status.HTTP_403_FORBIDDEN
            return "user already in use"
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
 

'''
II Nutzer anmelden und Spiel starten 
'''
@app.put("/api/v1/users/login")
async def login_user(user: PutUser, response: Response):
    try:
        try:
            user_df = load_users_from_csv()
        except:
            print("unable to load data from csv file") 

        if user.name not in list(user_df["name"]):
            response.status_code = status.HTTP_403_FORBIDDEN
            return "bad credentials"
        
        else:
            df = user_df.set_index("name", drop = False)
            if user.password in df.loc[user.name]["password"]:
                response.status_code = status.HTTP_202_ACCEPTED
                try:
                    #initiates question data frame 
                    question_df = load_questions_from_csv()
                    return "successful logged in"
                except:
                    print("unable to load data from csv file") 
            else:
                response.status_code = status.HTTP_401_UNAUTHORIZED
                return "wrong combination"
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


'''
III Fragen abrufen 
'''
@app.get("/api/v1/questions/{number_of_questions}", response_model = List[Question])
async def load_questions(*,number_of_questions: int = Path(title="The ID of the item to get", ge=1, le=len(load_questions_from_csv())), response:Response):
    try:
        question_df = load_questions_from_csv()
    except:
        print("unable to load data from csv file")
    
    try:
        question_list = []
        for sample in random.sample(range(0,len(question_df)),number_of_questions):
            question_list.append( {"question_id" : question_df.loc[sample, "id"], "question" : question_df.loc[sample, "question"], "options" : random.sample( question_df.loc[sample, "options"] + [question_df.loc[sample, "answer"]], 3 )  } )
        print(question_list)
        response.status_code = status.HTTP_200_OK
        return question_list
    
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return question_list

'''
IV Fragen hochladen und speichern
'''
@app.put("/api/v1/questions/add")
async def create_question(question: PutQuestion, response: Response):
    try:
        try:
            question_df = load_questions_from_csv()
        except:
            print("unable to load data from csv file")
        if question.question not in list(question_df["question"]):
            question_df.loc[len(question_df)] = [ max(list(question_df["id"]))+1, question.question, question.answer, question.options]
            response.status_code = status.HTTP_201_CREATED
            try:
                save_questions_to_csv(question_df)
            except:
                print("unable to save data to csv file")
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
async def add_answer(answer: PutAnswer, response: Response):
    try:
        question_df = load_questions_from_csv()
    except:
        print("unable to load questions from csv file")
    try:
        user_df = load_users_from_csv()
    except:
        print("unable to load user from csv file") 
    
    if answer.user_name not in list(user_df["name"]):
        response.status_code = status.HTTP_403_FORBIDDEN
        return "user not found"
    else:
        response.status_code = status.HTTP_201_CREATED
    #converts question_id to index
    df = question_df.set_index("id", drop = False)
    user_score = 0
    for new_answer in answer.answer:
        #checks time of answer check if question_id fits to answer string
        if new_answer.time < 20 and df.loc[new_answer.question_id]["answer"] == new_answer.answer:
            user_score +=1     
        else:
            user_score -=1
    
    user_df.at[list(user_df["name"]).index(answer.user_name),"score"] += user_score
    if user_df.at[list(user_df["name"]).index(answer.user_name),"score"] < 0:
        user_df.at[list(user_df["name"]).index(answer.user_name),"score"] = 0
    
    total_score = user_df.at[list(user_df["name"]).index(answer.user_name),"score"]
    try:
        save_user_to_csv(user_df)
        response.status_code = status.HTTP_201_CREATED
        
        return {"user_score":int(total_score)}
    except:
        print("unable to save user data to csv file")
    
    
    
        
        
    
    
        
    

'''
VI Punkteliste und Highscore aller Spieler abfragen
'''
#@app.get("/api/v1/users/highscore", response_model = List[Question])
@app.get("/api/v1/users/highscore", response_model=ScoringList)
async def return_highscores(response: Response):
    try:
        try:
            user_df = load_users_from_csv()
        except:
            print("unable to load data from csv file")            
        scoring_list = []
        for index, user in user_df.iterrows() :
            scoring_list.append({ "name" : user_df.loc[index, "name"], "score" : user_df.loc[index, "score"] })
        response.status_code = status.HTTP_200_OK
        return {"user" : scoring_list}
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22224, log_level='debug', reload = True)
