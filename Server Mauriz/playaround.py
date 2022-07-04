import pandas as pd

data = []
names = []
user_df = {}

user_df = pd.DataFrame(data, columns = [
    'user_name',
    'password',
    'score',
    ])


user_df = user_df.append({"user_name":"mo", "password":"xyz123", "score":0}, ignore_index=True) 
user_df = user_df.append({"user_name":"mau", "password":"xy3", "score":0}, ignore_index=True)
 
user_df = user_df.set_index("user_name", drop = False)
print(user_df.loc["mo"])
print(user_df.loc["mo"]["password"])
print("xyz123" in user_df.loc["mo"]["password"])


def login_user(user_name: str, password: str):
    if user_name not in list(user_df["user_name"]):
        #response.status_code = status.HTTP_403_FORBIDDEN
        return "bad credentials"
            
    else:
        df = user_df.set_index("user_name", drop = False)
        if password in df.loc[user_name]["password"]:
            #response.status_code = status.HTTP_202_ACCEPTED
            return "found username and password"
        else:
            #response.status_code = status.HTTP_401_UNAUTHORIZED
            return "wrong combination"

login_user("mo", "xyz123")
