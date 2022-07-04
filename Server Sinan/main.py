"""
Verteilte Anwendungen Gruppe 07 
Aufgabenblatt 02
1. Aufgabe


Members:
Mauriz Weymann, Sascha Heinze, Sinan Ertogrul, Mark Unger

Avengers Quiz mit Anmeldung / Registrierung
"""

# Start the application -> python -m uvicorn Quiz:app --reload

import Quiz
import Register
import questions
from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from typing import Union
import models
import json
import users
import uvicorn


app = FastAPI()

# Test Server
@app.get("/")
async def root():
    return {"Hallo: " "Ich bin ein Test"}

# Alle Nutzer anzeigen
@app.get("/api/v1/users/all")
async def get_all_users(response: Response):
    response.status_code = status.HTTP_202_ACCEPTED
    return users.all_users

@app.get("/api/v1/users/{user_name}")
async def get_user(name: str, response: Response):
    for u in range(len(users.all_users)):
        if users.all_users[u]["name"] == name:
            response.status_code = status.HTTP_200_OK
            return users.all_users[u]

# @app.get("/api/v1/users/{user_id}")
# async def get_user_id(user_id: int, response: Response):
#     for u in range(len(users.all_users)):
#         if users.all_users[u]["id"] == user_id:
#             response.status_code = status.HTTP_200_OK
#             return users.all_users[u]

# Nutzer anlegen und speichern
@app.put("/api/v1/users/add)")
async def create_user(data: models.User, response: Response):
    for existingNames in range(len(users.all_users)):
        if users.all_users[existingNames]["name"] == data.name:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"Error: " "Username already exists!"}
        elif data.highscore > 0:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"Error: " "Highscore is 0 by default, dont change the value!"}
        elif data.name == "UserName" or data.password == "Password":
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"Error: " "Please fill every field!"}
        
    else:
        response.status_code = status.HTTP_201_CREATED
        users.all_users.append(data) 
    return data

# Nutzer anmelden und Spiel starten --fehlt
@app.put("/api/v1/users/login")
async def login_user(name: str, password: str, response: Response):
    for us in range(len(users.all_users)):
        if users.all_users[us]["name"] == name and users.all_users[us]["password"] == password:
            response.status_code = status.HTTP_202_ACCEPTED
            return "Successful logged in"
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return "Wrong combination or User is not existing!"

# Alle Fragen abrufen
@app.get("/api/v1/questions/all")
async def load_questions(response: Response):
    response.status_code = status.HTTP_200_OK
    return questions.quiz

# Eine bestimmte Frage abrufen
@app.get("/api/v1/questions/{question_id}")
async def get_question(question_id: int, response: Response):
    for i in range(len(questions.quiz)):
        if questions.quiz[i]["id"] == question_id:
            return questions.quiz[i]     
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error: " "There is no question with the given id"}

# Neue Frage hochladen und speichern
@app.put("/api/v1/questions/add")
async def add_question(data: models.QuestionBuilder, response: Response):
    for ids in range(len(questions.quiz)):
        if questions.quiz[ids]["id"] == data.id:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"Question with this Id already exists! "}
        elif questions.quiz[ids]["question"] == data.question:
            return {"Error:" "Same question already exists! "}
        elif data.id < 0:
            return {"Error:" "Id must be greater than 0 "}
    if len(data.options) < 3:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error: " "You need 3 options!"}
    elif data.question == "Your Question":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error: " "Please type a real question!"}
    elif data.options == ["Option1"] or data.options == ["Option2"] or data.options == ["Option3"]: #Klappt noch nicht!
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error: " "Please define 3 different options!"}
    elif data.answer == "The answer of your question":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error: " "Please define a answer"}
    else:
        response.status_code = status.HTTP_201_CREATED
        questions.quiz.append(data)
    return data

# Antwort hochladen
@app.put("/api/v1/upload/answer")
async def upload_answer(answer: str, response: Response):
    return

# Punkteliste und Highscore aller Spieler abfragen
@app.get("/api/v1/highscores/all")
async def all_highscores():
    user_scores = []
    for highscores in users.all_users:
        usersc = {"name":highscores['name'], "highscore" :highscores['highscore']}
        user_scores.append(usersc)
    return user_scores

# Punkteliste von einem bestimmten Spieler
@app.get("/api/v1/highscores/{user_name}")
async def get_highscore(userName: str, response: Response):
    for i in range(len(users.all_users)):
        if users.all_users[i]["name"] == userName:
            return users.all_users[i]["highscore"]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error: " "There is no player with the given name!"}


# #User login or registration
# name = Register.collectcredentials()

# #Start Quiz 
# Register.update_user(name, Quiz.Game())

# #return Highscores
# Register.all_user_scores()


#register.collectcredentials()
# newscore = Quiz.Game()
# score = score + newscore