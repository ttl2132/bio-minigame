import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# need import the user name and time record from other module

# create the data model 
class Item(BaseModel):
    username: str 
    time: float

# create the app as an instance of the fastAPI class
app = FastAPI(debug = True)

# To create data withe the data model 
@app.post("/items")
async def create_item(item: Item):
    return item 

if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)