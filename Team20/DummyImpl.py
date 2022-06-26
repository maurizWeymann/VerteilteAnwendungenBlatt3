# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:02:03 2022

@author: 49177
"""

import json
'''
API III-GET Fragen Abrufen
ENDPUNKT /api/v1/questions/{num_question}
'''
getQuestions = "C:/Users/49177/git/htw/VerteilteAnwendung/VerteilteAnwendungenBlatt3/Team20/FragenAbrufenDummy.json"

with open(getQuestions) as fragen:
    fragen_list = json.load(fragen)

fragen = fragen_list['question']
for index,frage in enumerate(fragen):
    print(fragen[index]['question'])
    print(fragen[index]['Options'])
    
    
'''

'''
answer_filename = "C:/Users/49177/git/htw/VerteilteAnwendung/VerteilteAnwendungenBlatt3/Team20/AnswerDummy.json"    
answer = {
    "user_name" : "Mauriz",
    "answers":
        [
            {
            "ID" : 1, 
            "answer" : "Leo",
            "time" : "2022-06-26 20:24"
            },
            {
            "ID" : 2, 
            "answer" : "Mauriz",
            "time" : "2022-06-26 20:24"
            }
        ]
}

with open(answer_filename, 'w') as json_file:
    json.dump(answer, json_file, indent=4)
    