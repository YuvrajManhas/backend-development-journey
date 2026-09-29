from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TodoCreate(BaseModel):
    title : str
    completed : bool = False

class TodoUpdate(BaseModel):
    title : str
    completed : bool

todos = []

@app.get("/")
def home():
    return {"message" : "Welcome to Todo API"}

@app.post("/todos")
def post_todo(todo : TodoCreate):
    new_todo = {
        "id" : len(todos) + 1,
        "title" : todo.title,
        "completed" : todo.completed
    }

    todos.append(new_todo)

    return new_todo

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id : int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    return {"message" : "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id : int, todo_update : TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = todo_update.title
            todo["completed"] = todo_update.completed
            return todo

    return {"message" : "Todo not found!"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id : int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message" : "Todo deleted successfully!"}

    return {"message" : "Todo does not exist."}