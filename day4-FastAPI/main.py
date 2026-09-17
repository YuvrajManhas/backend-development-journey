from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Student API"
    }

@app.get("/students")
def get_students():
    return {
        "students": [
            "Yuvraj",
            "Rahul",
            "Aman"
        ]
    }

@app.get("/about")
def about():
    return {
        "project": "Student API",
        "technology": "FastAPI"
    }

@app.post("/students")
def create_student():
    return {
        "message": "Student created successfully"
    }

@app.put("/students")
def update_student():
    return {
        "message": "Student updated successfully"
    }

@app.delete("/students")
def delete_student():
    return {
        "message": "Student deleted successfully"
    }