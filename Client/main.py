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

URL = "http://localhost:22224/"

'''
starts the overall login or registration process, return user name
'''
def collectcredentials():
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
        password = input("Enter Password: ")
        try:
            payload=json.dumps({"name" : name, "password" : password})
            headers={"Content-Type": "application/json"}
            response = requests.request("PUT", URL + "api/v1/users/login", headers=headers, data=payload)
            #print(f"Status: {response.status_code}, Data: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Server not found: {e}'")
        if response.status_code == 202:
            print(response.json())
            time.sleep(2)
        elif response.status_code == 401:
            print(response.json())
            print('please try again')
            time.sleep(2)
            login()     
        elif response.status_code == 403:
            print(response.json())
            print('please try again')
            time.sleep(2)
            login()
            
        StartGame(name)
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
    password = input("Choose Password: ")
    try:
        payload=json.dumps({"name" : name, "password" : password})
        headers={"Content-Type": "application/json"}
        response = requests.request("PUT", URL + "api/v1/users/add", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
    
    if response.status_code == 201:
        print(response.json())
        time.sleep(2)
        StartGame(name)
    elif response.status_code == 403:
        print(response.json())
        time.sleep(2)
        print('please try again')
        collectcredentials()     
       
def StartGame(name):
    questions = getQuestions()
    countdown(3)
    answers = quiz(questions)
    pushAnswer(name, answers)
    os.system('cls')
    print(f"Thanks for playing {name}! 💜\n\n")
    getHighscore()

def quiz(questions):
    answer_list = []
    for question in questions:
        os.system('cls')
        startTimer = time.time()
        print(question["question"])
        print(f'a) {question["options"][0]} b) {question["options"][1]} c) {question["options"][2]} ')
        choive_eval= False
        choice = input("Answer: ").lower()
        if choice == "a" or choice == "b" or choice == "c":
            choive_eval= True
        print(choive_eval)
        while choive_eval == False:
            print('Just letters a, b or c allowed')
            choice = input("Answer: ").lower()
            if choice == "a" or choice == "b" or choice == "c":
                choive_eval= True
            print(choice)
                
        duration = round(time.time() - startTimer, 2)
        if choice == "a":
            choice = choice.replace("a", f'{question["options"][0]}')
        if choice == "b":
            choice = choice.replace("b", f'{question["options"][1]}')
        if choice == "c":
            choice = choice.replace("c", f'{question["options"][2]}')
            
        
        answer_list.append({"question_id":question["question_id"], "answer": choice, "time":duration})
        #print(answer_list)
    return answer_list 

def getQuestions():
    """
    Introduces user to the quiz and rules.
    """
    os.system('cls')
    print("Welcome to this fun quiz! \n")
    print(f"Please choose a number of questions you would like to quiz. \nMax number between 1-10. \nAnswers that take more than 20s count as FALSE!")
    
    tmplStr = f"\nPlease insert the number of questions you want to be asked up to 10 questions possible: "
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
        response = requests.request("GET", URL + f"api/v1/questions/{qs}", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
        
    return response.json()

     
def pushAnswer(name, answer):
    try:
        payload=json.dumps({"user_name" : name, "answer" : answer})
        headers={"Content-Type": "application/json"}
        response = requests.request("PUT", URL + "api/v1/answer", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
    
def getHighscore():
    try:
        payload={}
        headers={"Content-Type": "application/json"}
        response = requests.request("GET", URL + f"api/v1/users/highscore", headers=headers, data=payload)
        #print(f"Status: {response.status_code}, Data: {response.json()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}'")
    
    print('HighscoreList:\n-------------') 
    scoring_list = response.json()
    for user in scoring_list["user"]:
        user_name = user["name"]
        user_score = str(user['score'])
        print(f"{user_score.rjust(3,' ')} - {user_name}")
    print('-------------') 
    
def countdown(timer):
    """

    Args:
        timer (int): sets the time for the countdown until game starts
    """
    cd = timer
    for x in range(timer):
        print(cd)
        cd-=1
        time.sleep(1) # Sleep for 3 seconds
        os.system('cls')
        
#StartGame("mauriz")
#getHighscore()
collectcredentials()

'''
def check_ans(question, answer, score, Zeit):

    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """l
    if quiz[question]['answer'].lower() == answer.lower():
        print(f"Correct Answer! ({int(Zeit)}s) \nScore +1!\n")
        return True
    else:
        print(f"Wrong Answer :( \nScore -1\n")
        return False




def Game():
    """
    Quiz starts after a short countdown. 
    When the number of questions given by the user was quized, the game will stop and present your score.
    This score will be returned to be processed afterwards.   

    Returns:
        score: reached score will be returned to be added to users highscore
    """
    questions = intro_message()
    os.system('cls')
    while True:
        a = 0
        score = 0
        qindex = random.sample(range(1,quiz.__len__()+1), questions) 
        #print(qindex)
        countdown(3)
        for question in quiz:
            while a < questions:
        
                os.system('cls')
                print("Answer must be written in words!\n")
                print(quiz[qindex[a]]['question'])
                print("\n")
                b = 0
                for x in random.sample(range(0,3),3):
                    if b == 0 :
                        print(f"a)\t{quiz[qindex[a]]['options'][x]}")
                    elif b == 1:
                        print(f"b)\t{quiz[qindex[a]]['options'][x]}")
                    else:
                        print(f"c)\t{quiz[qindex[a]]['options'][x]}")
                    b +=1
                print("\n")
                Start = dt.datetime.now()
                answer = input()
                os.system('cls')
                Ende =  dt.datetime.now()
                Zeit = (Ende-Start).total_seconds()
                if Zeit < 20.00:
                    check = check_ans(qindex[a], answer, score, Zeit)
                else:
                    check = False
                    print(f"Zu langsam! ({int(Zeit)}s)\nScore -1\n")
                a +=1
                time.sleep(2)
                if check:
                    score += 1
                    break
                # if score >= 1:
                score -= 1
                
                
        break

    os.system('cls')
    print(f"Your final score is {score}!\n\n")
    print("Thanks for playing! 💜\n\n")
    return score

'''