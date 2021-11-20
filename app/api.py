from typing import List
from fastapi import FastAPI

from model.user import User
from model.order import Order

app = FastAPI()

handler = DBHandler() 

@app.get("/get/allorders/", response_model=List[Order])
async def get_all_orders():
    return handler.get_all_orders()

@app.get("/get/allusers/", response_model=List[User])
async def get_all_users():
    return handler.get_all_users()

@app.post("/post/order/")
async def create_order(order: Order):
    # order_handler.create(order)
    return order

@app.post("/post/user/")
async def create_user(user: User):
    # user_handler.create(user)
    return user
