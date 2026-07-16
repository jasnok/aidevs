
"""
uvicorn 00_request:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Request Test",
    description="Request Test",
    version="0.0.1",

)


class Customor(BaseModel):
    id : str
    pwd : str
    name : str
    age : str

@app.get("/health")
def health():
    return {"msg":"OK"}

@app.post("/register")
def register(customer:Customor):
    print(customer.id)
    print(customer.pwd)
    print(customer.name)
    print(customer.age)
    return {"msg":"가입축하!"}

