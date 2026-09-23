
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=1, le=120)
    email: EmailStr


class Address(BaseModel):
    city: str
    state: str
    pincode: int


class Student(BaseModel):
    name: str
    age: int
    address: Address


class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


class Order(BaseModel):
    order_id: int
    customer_name: str
    items: list[Item]


@app.get("/")
def home():
    return {"message": "Day 6 Pydantic API is running"}


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user.model_dump(mode="json")
    }


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student.model_dump()
    }


@app.post("/orders")
def create_order(order: Order):
    total = 0

    for item in order.items:
        total += item.price * item.quantity

    return {
        "message": "Order created successfully",
        "order": order.model_dump(),
        "total": total
    }