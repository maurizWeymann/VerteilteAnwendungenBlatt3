from questions import quiz
import os
import random
import datetime as dt
import time
import main

global answer
global score



def check_ans(question, answer, score, Zeit):

    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == answer.lower():
        print(f"Correct Answer! ({int(Zeit)}s) \nScore +1!\n")
        return True
    else:
        print(f"Wrong Answer :( \nScore -1\n")
        return False

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

def intro_message():
    """
    Introduces user to the quiz and rules.
    """
    os.system('cls')
    print("Welcome to this fun quiz! \n")
    print(f"There is a total of {quiz.__len__()} questions. Answers that take more than 20s count as FALSE!")
    
    tmplStr = f"\nPlease insert the number of questions you want to be asked up to {quiz.__len__()} questions: "
    qs = False
    while not qs:
        user_input = input(tmplStr) #asks user to set the number of questions
        try:
            qs = int(user_input)
            if qs > quiz.__len__():
                qs = False
                raise ValueError
        except ValueError:
               print("Oops!  That was no valid number.  Try again...!")
    return qs

def Game():
    """
    Quiz starts after a short countdown. 
    When the number of questions given by the user was asked, the game will stop and present your score.
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

