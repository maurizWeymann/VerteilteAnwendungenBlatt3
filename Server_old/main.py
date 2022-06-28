"""
Created on Wed Jun 15 14:29:15 2022

@author: mauriz

type the following in your terminal to start the server
python -m uvicorn server:app --reload
"""
from fastapi import FastAPI, status, Response, HTTPException
from mydata import MyInventoryPostElement, MyInventoryElement, MyInventory
from typing import List
import uvicorn

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/docs",
    title="Demo Rest",
    version="1.0",
    openapi_url="/api/v1/openapi.json"
)

data = MyInventory()

data.add_element(MyInventoryElement(name = "cup", quantity = 100))
data.add_element(MyInventoryElement(name = "chair", quantity = 3))
data.add_element(MyInventoryElement(name = "table", quantity = 6))

# CRUD
# CREATE, READ, UPDATE, DELETE

@app.get("/")
async def test():
    message = "hello"
    print(message)
    # raise HTTPException(status_code=409, detail="Nickname already registered")
    return message

'''
@app.get("/v1/items", response_model=List[MyInventoryElement])
async def read_all_items():
    return data.get_elements()

@app.get("api/v1/users/highscore", response_model=MyInventoryElement)
async def all_user_scores():
    data = load_all_data()
    user_scores = []
    for user in data:
        users = {"name":user['name'], "highscore" :user['highscore']}
        user_scores.append(users)
    return user_scores 
'''

'''
    print('HighscoreList:\n-------------')    
    for user in sorted(user_scores, key = lambda item: item['highscore'], reverse=True):
        user_name = user['name']
        user_score = str(user['highscore'])
        print(f"{user_score.rjust(3,' ')} - {user_name}")
    print('-------------')  
'''

'''
@app.put("api/v1/answer}", response_model=MyInventoryElement, status_code = 200)
async def update_user(user_name, score):
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
        json.dump(data, json_file, indent=4

@app.delete("/v1/items/{item_id}", response_model=int)
async def delete_item(item_id: int):
    return data.remove_element(item_id)

@app.post("/v1/items", response_model=MyInventoryElement, status_code = 201)
async def create_item(item : MyInventoryPostElement):
    return data.add_element(MyInventoryElement(name = item.name, quantity = item.quantity))

'''
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22222, log_level='debug', reload=True)

