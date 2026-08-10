from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Nested Model
# {
#     "name":"Naga",
#     "address":{
#         "city":"Hyderabad",
#         "pin":500001
#     }
# }
# {
#     "name": "Naga",
#     "age": "25" 
#     # Pydantic will automatically convert compatible types."25"  →  25. Pydantic cannot convert it."age": "Twenty Five"
# } 
class Address(BaseModel):
    city: str
    pin: int


class User(BaseModel):
    name: str
    address: Address

class Employee(BaseModel):
    name: str
    department: str
    salary: float
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 101,
        "name": "Naga",
        "age": 30,
        "password": "abc123"
    }
    
@app.get("/users/{user_id}")
def get_user(user_id: int): # user_id is automatically extracted.
    return {"id": user_id}

# . Query Parameters
# /search?name=Naga&age=30
@app.get("/search")
def search(name: str, age: int): # This(parameters) validation is handled by Pydantic, not by your code.
    return {
        "name": name,
        "age": age
    }

@app.get("/")
async def home():
    data = await get_data()
    return data

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

@app.get('/weather')
def weather(lat: float, lon: float):
    return {
        "latitude": lat,
        "longitude": lon
    }


@app.post("/employee")
def create_employee(emp: Employee):
    return {
        "message": "Employee Created",
        "employee": emp
    }