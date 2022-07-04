from textwrap import indent
from user import *
import json
import os
import time


filename = 'user.json'
os.system('cls')

#starts the overall login or registration process, return user name
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
    

#logs in for user if possible, return user name 
def login():
    os.system('cls')
    print('If you want to exit, simply write \'exit\'.')
    name = input("Enter Username: ")
    if name != 'exit':
        password = input("Enter Password: ")
        if check_credentials(name, password):
            load_user(name)
        else:
            print('Combination of User and Password not found! \n please try again.')
            time.sleep(2)
            login()
        return name
    else:
        collectcredentials()

#registration for user if possible, return user
def register():
    name = input("Choose Username: ")
    if len(name) > 10:
        os.system('cls')
        print('Name to long, please choose shorter name')
        register()
    password = input("Choose Password: ")
    new_user = {'name': name,'password': password, 'highscore': 0}
    register_new_user(new_user)
    return name

#checks for valid credentials, return true or false
def check_credentials(user_name, password):
    data = load_all_data()
    if user_name not in all_user_names():
        return False
    for user in data:
        if user_name in user['name'] and password in user['password']:
            return True

#loads user from file and creates user object
def load_user(user_name):
    data = load_all_data()
    if user_name in all_user_names():
        for user in data:
            if user['name'] in user_name:
                global playing_user
                playing_user = User(user['name'],user['password'],user['highscore']) 
                print(f'{playing_user.name} -> Ready to Play!')
                return 
    print('User not registered yet!')
    time.sleep(2)
    return

#updates user score and writes to file
def update_user(user_name, score):
    data = load_all_data()
    for user in data:
        if user_name in user['name']:
            user_highscore = user['highscore']
            user_highscore += score
            if user_highscore < 0:
                user['highscore'] = 0
            else:
                user['highscore'] = user_highscore
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

#loads all saved user information from file
def load_all_data():
    with open(filename) as all_user:
        user_list = json.load(all_user)
    return user_list

def user_json(user_data):
    user_as_json = json.dumps(user_data,default=encoder_user)
    return user_as_json

def encoder_user(user):
    return {"name":user.name,"password":user.password,"highscore":user.highscore}

#saves a new user if name does not exists yet
def register_new_user(new_user):
  if new_user['name'] not in all_user_names():
    save_new_user(new_user)
  else:
    print('Username bereits vergeben!')
    time.sleep(2)
    register()

#adds user to list and saves list to file
def save_new_user(user):
    # Write to File
    data = load_all_data()
    data.append(user)
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

#returns a list of all user names
def all_user_names():
  data = load_all_data()
  user_names = [ user['name'] for user in data]
  return user_names

#returns a list of all user names
def all_user_scores():
    data = load_all_data()
    user_scores = []
    for user in data:
        users = {"name":user['name'], "highscore" :user['highscore']}
        user_scores.append(users)
    print('HighscoreList:\n-------------')    
    for user in sorted(user_scores, key = lambda item: item['highscore'], reverse=True):
        user_name = user['name']
        user_score = str(user['highscore'])
        print(f"{user_score.rjust(3,' ')} - {user_name}")
    print('-------------')  
   
