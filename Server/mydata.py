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
    user_name : str
    answer : list[Answer]

class UserScore(BaseModel):
    name : str
    score : int
    
class ScoringList(BaseModel):
    user : list[UserScore]    
    

