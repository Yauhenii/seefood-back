from typing import List
from fastapi import FastAPI, HTTPException
import psycopg2 as ps

from model.user import User
from model.order import Order
from model.category import Category
from db.order_handler import OrderHandler
from db.user_handler import UserHandler
from db.category_handler import CategoryHandler

app = FastAPI()

order_handler = OrderHandler(
    host="127.0.0.1",
    port="5432",
    user_name="postgres",
    password="5432",
    table_name="seefood.order",
    table_user_name="seefood.user",
    table_category_name="seefood.category",
)

user_handler = UserHandler(
    host="127.0.0.1",
    port="5432",
    user_name="postgres",
    password="5432",
    table_name="seefood.user",
)

category_handler = CategoryHandler(
    host="127.0.0.1",
    port="5432",
    user_name="postgres",
    password="5432",
    table_name="seefood.category",
)


# @app.get("/get/allorders/", response_model=List[Order])
# async def get_all_orders():
#     return order_handler.

######
# USER
######


@app.get("/user/get/all", response_model=List[User])
async def get_user_all():
    try:
        user_list = user_handler.select_all_user()
        return user_list
    except IndexError:
        raise HTTPException(status_code=404, detail="no users found")


@app.get("/user/get/by-login/{login_name}", response_model=User)
async def get_user_by_login(login_name):
    try:
        user = user_handler.select_user_by_login([login_name])
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="no user found")


@app.delete("/user/delete/by-login/{login_name}", response_model=User)
async def delete_user_by_login(login_name):
    try:
        user = user_handler.delete_user_by_login([login_name])
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="no user found")


@app.post(
    "/user/post/login_name={login_name},full_name={full_name},address_name={address_name},phone_number={phone_number}"
)
async def create_user(login_name, full_name, address_name, phone_number):
    try:
        user = user_handler.insert_user(
            [login_name, full_name, address_name, phone_number]
        )
        return user
    except ps.errors.UniqueViolation:
        raise HTTPException(status_code=404, detail="this login name already exists")


##########
# Category
##########


@app.get("/category/get/by-name/{category_name}", response_model=Category)
async def get_category_by_name(category_name):
    try:
        category = category_handler.select_category_by_name([category_name])
        return category
    except IndexError:
        raise HTTPException(status_code=404, detail="no category found")


@app.get("/category/get/all", response_model=List[Category])
async def get_category_all():
    try:
        category_list = category_handler.select_all_category()
        return category_list
    except IndexError:
        raise HTTPException(status_code=404, detail="no categories found")


@app.delete("/category/delete/by-name/{category_name}", response_model=Category)
async def delete_category_by_name(category_name):
    try:
        category = category_handler.delete_category_by_category_name([category_name])
        return category
    except IndexError:
        raise HTTPException(status_code=404, detail="no category found")


@app.post("/user/post/category_name={category_name},avg_calories={avg_calories}")
async def create_user(category_name, avg_calories):
    try:
        category = category_handler.insert_category([category_name, avg_calories])
        return category
    except ps.errors.UniqueViolation:
        raise HTTPException(status_code=404, detail="this category already exists")


##########
# ORDER
##########

@app.get("/order/get/by-id/{id}", response_model=Order)
async def get_order_by_id(id):
    try:
        order = order_handler.select_order_by_id([id])
        return order
    except IndexError:
        raise HTTPException(status_code=404, detail="no order found")

@app.get("/order/get/all", response_model=List[Order])
async def get_order_all():
    try:
        order_list = order_handler.select_all_order()
        return order_list
    except IndexError:
        raise HTTPException(status_code=404, detail="no orders found")


@app.post(
    "/user/post/login_name={login_name},food_name={food_name},category_name={category_name},price={price},due_date={due_date},comment={comment},is_anonymus={is_anonymus},is_completed={is_completed},is_trashed={is_trashed}"
)
async def create_order(
    login_name,
    food_name,
    category_name,
    price,
    due_date,
    comment,
    is_anonymus,
    is_completed,
    is_trashed,
):
    try:
        order = order_handler.insert_order_by_login_name_and_category(
            [
                login_name,
                food_name,
                category_name,
                price,
                due_date,
                comment,
                is_anonymus,
                is_completed,
                is_trashed,
            ]
        )
        return order
    except ps.errors.NotNullViolation:
        raise HTTPException(status_code=404, detail="invalid login or category name")

@app.delete("/order/delete/by-id/{id}", response_model=Order)
async def delete_order_by_id(id):
    try:
        order = order_handler.delete_order_by_id([id])
        return order
    except IndexError:
        raise HTTPException(status_code=404, detail="no order found")
