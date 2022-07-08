from typing import Optional, Union
from pydantic import BaseModel
import json

class User(BaseModel):
    id : Optional[int] = None
    name : str
    password : str
    score : Optional[int]

class PutUser(BaseModel):
    name : str
    password : str

class Question(BaseModel):
    question_id : int
    question : str
    options : list[str]

class PutQuestion(BaseModel):
    question : str
    answer : str
    options : list[str]

class Answer(BaseModel):
    question_id : int
    answer : str
    time : float

class PutAnswer(BaseModel):
    answer : list[Answer]

class UserScore(BaseModel):
    name : str
    score : int
    
class ScoringList(BaseModel):
    user : list[UserScore]    
    


    

class MyUsers:
    def __init__(self):
        self.elements = list()
        self.id = 0

    def add_user(self, element : User, put = False) -> int:
        if put and element.id > 0:
            self.id = element.id
        else:
            self.id += 1
            element.id = self.id
        
        self.elements.append(element)
        return element

    def add_element(self, element : User, put = False) -> int:
        if put and element.id > 0:
            self.id = element.id
        else:
            self.id += 1
            element.id = self.id
        
        self.elements.append(element)
        return element
    
    def remove_element(self, id : int) -> int:
        t_elements = self.elements[:]
        for t_element in t_elements:
            if t_element.id == id:
                self.elements.remove(t_element)
                return id
        return 0
    
    def get_elements(self) -> list:
        return self.elements
    
    def get_questions(number_of_questions) -> list:
        #loads all saved questions from file
        with open('question.json') as all_questions:
            question_list = json.load(all_questions)
        return question_list
    
    def get_element(self, id : int) -> User:
        for element in self.elements:
            if element.id == id:
                return element
        return 0
    
    # state 0 change, status 1 new
    def update_element(self, id : int, element : User):
        state = 1
        t_elements = self.elements[:]
        print(id)
        for t_element in t_elements:
            if t_element.id == int(id):
                element.id = int(id)
                self.elements[self.elements.index(t_element)] = element
                state = 0
                print("done")
                return (state, element)
        
        element.id = int(id)
        element = self.add_element(element, True)
        return (state, element)
         
    def get_max_id(self) -> int:
        return self.id
