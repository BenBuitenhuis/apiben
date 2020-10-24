from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def root():
    return{'message':'Hallo Wereld'}

@app.get("/ben/{item_id}")
async def read_idtem(item_id):
    if item_id == "Ben Buitenhuis":
        return{"message":"Welkom meneer Buitenhuis"}
    else:
        s = f'Hallo {item_id}'
        return json.dumps({f"message":s})

