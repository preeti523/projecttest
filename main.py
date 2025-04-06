#program
=======
from fastapi import FastAPI
app = FastAPI()

@app.get("/First")
def index():
    return "Hello, world!"

#create http://myntra.com/items/item_id

@app.get("/items/{item_id}")
def index(item_id:int):
    return {"product_id":item_id}

@app.get("/items/")
def index(q:int=0):
    return {"product is":q}

