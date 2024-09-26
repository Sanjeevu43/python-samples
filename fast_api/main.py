from fastapi import FastAPI, Request
from pydantic import BaseModel

class Person(BaseModel):
        id:int
        name:str

app = FastAPI()

@app.get('/{name}')
def getMessage(name: str):
    return "Hello " + name

# @app.post('/{item}')
# def getMessage(item: str):
#     return "item is " + item

@app.post('/person')
def person_data(p: Person):
    #person_data = request.json();
    return p
    
    