import requests
import json

URL = "http://localhost:22224/"

def main():
    print("Read Data:")
    try:
        response = requests.get(URL + "?param=name")
        print(f"Status: {response.status_code}, Data: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Server not found: {e}")

    


    # try:
    #     response = requests.get(URL + "v1/items")
    #     print(f"Status: {response.status_code}, Data: {response.json()}")
    # except requests.exceptions.RequestException as e:
    #     print(f"Server not found: {e}")

    
    # data = json.dumps({
    #     "name": "new object",
    #     "quantity": 9,
    #     "id": 0
    #     })
    # print("Add Data:")
    # headers = {"Content-Type": "application/json"}
    # response = requests.put(URL + "v1/items/0", data=data, headers=headers)
    # print(f"Status: {response.status_code}, Data: {response.text}")
    
    # data = json.dumps({
    #     "name": "new object",
    #     "quantity": 10,
    #     })

    # print("Add Data Post:")
    # headers = {"Content-Type": "application/json"}
    # response = requests.post(URL + "v1/items", data=data, headers=headers)
    # print(f"Status: {response.status_code}, Data: {response.text}")

    # print("Delete Data: ")
    # response = requests.delete(URL + "v1/items/3")
    # print(f"Status: {response.status_code}, Data: {response.text}")

if __name__ == '__main__':
    main()