# -*- coding: utf-8 -*-
'''
Intalliert alle nowendigen Pakete
    pip install -r requirements.txt
    
Erzeugt requirements.txt
python -m pip freeze > requirements.txt

API Explanation
https://rapidapi.com/apidojo/api/transfermarket

'''

import os
import random
import datetime as dt
import time

global answer
global score
import requests
import json

URL = "http://localhost:22222/"

'''
starts the overall login or registration process, return user name
'''
def collectcredentials():
    os.system('cls')
    flag = False
    while flag == False:
        login_or_register = input("Type Login or Register: ").lower()
        if  'login' in login_or_register or 'register' in login_or_register:
            flag = True
            os.system('cls')
            if login_or_register == 'login':
                name = login()
            elif login_or_register == 'register':
                name = register()
                #return name
        else:
            os.system('cls')
            print('Please check spelling and try again')
    return name
'''
logs in for user if possible, return user name 
'''
def login():
    os.system('cls')
    print('If you want to exit, simply write \'exit\'.')
    name = input("Enter Login Username: ")
    if name != 'exit':
        #password = input("Enter Password: ")
        try:
            name = "string"
            payload=json.dumps({})
            headers={"Content-Type": "application/json"}
            response = requests.request("GET", URL + "v1/users/name/"+str(name), headers=headers, data=payload)
            #print(f"Status: {response.status_code}, Data: {response.json()}")
            data = response.json()[0]
            #print(data["ID"])
        except requests.exceptions.RequestException as e:
            print(f"Server not found: {e}'")
        if response.status_code == 200:
            #print(response.json())
            time.sleep(2)
        else:
            time.sleep(2)
            login()
            
        StartGame(name, data["ID"] )
    else:
        collectcredentials()

'''
checks for valid credentials, return true or false
'''
def check_credentials(user_name, password):
    try:
        payload=json.dumps({"name" : user_name, "password" : password})
        headers={"Content-Type": "application/json"}
        response = requests.request("PUT", URL + "api/v1/users/login", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
    if response.status_code == 202:
        print(response.json())
        return True
    elif response.status_code == 401:
        print(response.json())
        return False
    elif response.status_code == 403:
        print(response.json())
        return False
'''
registration for user if possible, return user
'''
def register():
    name = input("Choose Username: ")
    if len(name) > 10:
        os.system('cls')
        print('Name to long, please choose shorter name')
        register()
    #password = input("Choose Password: ")
    try:
        name = "string"
        payload=json.dumps({"name" : name, "score" : 100})
        headers={"Content-Type": "application/json"}
        response = requests.request("POST", URL + "v1/users", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
    
    if response.status_code == 200:
        print("your name is registered now")
        time.sleep(2)
        login()
    elif response.status_code == 404:
        print(response.json())
        time.sleep(2)
        print('please try again')
        collectcredentials()     
       
def StartGame(name, user_id):
    questions = getQuestions()
    countdown(3)
    answers = quiz(questions)
    pushAnswer(user_id, name, answers)
    os.system('cls')
    print(f"Thanks for playing {name}! 💜\n\n")
    getHighscore()

def quiz(questions):
    answer_list = []
    
    for question in questions:
        os.system('cls')
        startTimer = time.time()
        print(question["Question"])
        print(f'a) {question["Answer1"]} b) {question["Answer2"]} c) {question["Answer3"]} ')
        choive_eval= False
        choice = input("Answer: ").lower()
        if choice == "a" or choice == "b" or choice == "c":
            choive_eval= True
        
        while choive_eval == False:
            print('Just letters a, b or c allowed')
            choice = input("Answer: ").lower()
            if choice == "a" or choice == "b" or choice == "c":
                choive_eval= True
            
                
        duration = round(time.time() - startTimer, 2)
        if choice == "a":
            choice = choice.replace("a", "1")
        if choice == "b":
            choice = choice.replace("b", "2")
        if choice == "c":
            choice = choice.replace("c", "3")
            
        
        answer_list.append({"question_id":question["ID"], "answer": choice})
        #print(answer_list)
    return answer_list 

def getQuestions():
    """
    Introduces user to the quiz and rules.
    """
    os.system('cls')
    print("Welcome to this fun quiz! \n")
    print(f"Please choose the number of questions you would like to quiz. \nMax number of questions between 1-10. \nTime to answer each question - less than 20s!")
    
    tmplStr = f"\nEnter number of questions, max 10 questions possible: "
    qs = False
    while not qs:
        user_input = input(tmplStr) #asks user to set the number of questions
        try:
            qs = int(user_input)
            if qs > 10:
                qs = False
                raise ValueError
        except ValueError:
               print("Oops!  That was no valid number.  Try again...!")
    try:
        payload={}
        headers={"Content-Type": "application/json"}
        response = requests.request("GET", URL + f"v1/questions/amount/{qs}", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
        
    return response.json()

     
def pushAnswer(user_id, name, answers):
    for answer in answers:
        try:
            
            payload={}
            headers={}
            response = requests.request("POST", URL + f"v1/answer/{answer['question_id']}/{answer['answer']}/{name}", headers=headers, data=payload)
            #print(f"Status: {response.status_code}, Data: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Server not found: {e}'")
        
def getHighscore():
    try:
        payload={}
        headers={"Content-Type": "application/json"}
        response = requests.request("GET", URL + f"v1/users", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
        
    
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
    
    print('HighscoreList:\n-------------') 
    scoring_list = response.json()
    for user in scoring_list:
        user_name = user["Name"]
        user_score = str(user['Score'])
        print(f"{user_score.rjust(3,' ')} - {user_name}")
        
    print('-------------') 
    
def countdown(timer):
    """

    Args:
        timer (int): sets the time for the countdown until game starts
    """
    os.system('cls')
    cd = timer
    for x in range(timer):
        print(cd)
        cd-=1
        time.sleep(1) # Sleep for 3 seconds
        os.system('cls')
        
if __name__ == '__main__':
    collectcredentials()