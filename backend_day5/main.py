from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title = "Day 5 - User Management API")

class User(BaseModel):
    name : str
    age : int
    email : str

class UserResponse(User):
    id : int

users = [
    {
        "id": 1,
        "name": "Yuvraj",
        "age": 20,
        "email": "yuvraj@example.com"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 21,
        "email": "rahul@example.com"
    },
    {
        "id": 3,
        "name": "Aman",
        "age": 20,
        "email": "aman@example.com"
    }
]

@app.get("/")
def home():
    return {"message" : "Welcome to User Management API"}

@app.get("/users", response_model=list[UserResponse])
def get_users(age : int | None = None):
    if age is None:
        return users

    filtered_users = []

    for user in users:
        if user["age"] == age:
            filtered_users.append(user)

    return filtered_users

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id : int):
    for user in users:
        if(user["id"]) == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User Not Found!"
    )

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user : User):
    new_id = len(users) + 1

    new_user = {
        "id" : new_id,
        "name" : user.name,
        "age" : user.age,
        "email" : user.email
    }

    users.append(new_user)

    return new_user
