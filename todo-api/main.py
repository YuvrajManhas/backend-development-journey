from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoUpdate(BaseModel):
    title: str
    completed: bool

todos = [
    {
        "id" : 1,
        "Title" : "Learn Python",
        "Completed" : "True"
    },
    {
        "id" : 2,
        "title" : "Learn REST APIs",
        "completed" : "False"
    }
]

@app.get("/")
def home():
    return{"message" : "TODO Api is running!"}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id : int):

    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    return {"message" : "Todo not found."}

@app.post("/todos")
def create_todo(todo: TodoCreate):

    new_todo = {
        "id" : len(todos) + 1,
        "Title" : todo.title,
        "completed" : todo.completed
    }

    todos.append(new_todo)

    return new_todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id : int, updated_todo : TodoUpdate):

    for todo in todos:

        if todo["id"] == todo_id:

            todo["Title"] = updated_todo.title
            todo["completed"] = updated_todo.completed

            return todo

    return {"message" : "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id : int):

    for todo in todos:

        if todo["id"] == todo_id:
            todos.remove(todo)

            return {"message" : "Todo deleted"}

    return {"message" : "Todo not found"}



