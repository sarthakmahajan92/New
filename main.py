from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List 


app = FastAPI()

# GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Gammaedge"}

# GET endpoint 
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    price: List[float]
    items:List[str]

@app.post("/items/")
def create_item(item: Item):   #
    return {"name": item.name, "price": item.price , "items": item.items}  #Payload is usaully JSON body data sent in a request.


# PUT endpoint
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}

# DELETE endpoint
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}       
