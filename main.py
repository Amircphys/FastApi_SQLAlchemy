from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn


app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {"message": "Hello index!!!"}


@app.get("/hello")
def hello(name: str = "world"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users")
def create_user(user: CreateUser):
    return {"message": {"status": "success", "email": user.email}}


@app.get("/items")
def get_items():
    return ["item_1", "item_2"]


@app.get("/items/latest")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item": {"id": item_id}}


@app.post("/calc/add")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
