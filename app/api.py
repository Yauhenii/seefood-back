from typing import List
from fastapi import FastAPI

from model.user import User
from model.order import Order
from db_handler import DBHandler

app = FastAPI()

handler = DBHandler() 

@app.get("/getAllOrders/", response_model=List[Order])
async def get_all_orders():
    return handler.get_all_orders()

@app.get("/getAllUsers/", response_model=List[User])
async def get_all_users():
    return handler.get_all_users()