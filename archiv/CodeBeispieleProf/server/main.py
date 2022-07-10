from fastapi import FastAPI, status, Response, HTTPException
from mydata import MyInventoryElement, MyInventory, MyInventoryPostElement
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

@app.get("/", response_model=str)
async def test(param : str):
    print(param)
    # raise HTTPException(status_code=409, detail="Nickname already registered")
    return param


@app.get("/v1/items", response_model=List[MyInventoryElement])
async def read_all_items():
    return data.get_elements()

@app.get("/v1/items/{item_id}", response_model=MyInventoryElement)
async def read_item(item_id: int):
    return data.get_element(item_id)

@app.put("/v1/items/{item_id}", response_model=MyInventoryElement, status_code = 200)
async def change_item(item_id, element: MyInventoryElement, response : Response):
    state, element = data.update_element(item_id, element)
    print("Status: " , state)
    if state == 1:
        response.status_code = status.HTTP_201_CREATED
    return element 

@app.delete("/v1/items/{item_id}", response_model=int)
async def delete_item(item_id: int):
    return data.remove_element(item_id)

@app.post("/v1/items", response_model=MyInventoryElement, status_code = 201)
async def create_item(item : MyInventoryPostElement):
    return data.add_element(MyInventoryElement(name = item.name, quantity = item.quantity))


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=22222, log_level='debug', reload=True)
