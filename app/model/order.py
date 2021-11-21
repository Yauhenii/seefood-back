from pydantic import BaseModel
from datetime import date as dt

from model.category import Category
from model.user import User


class Order(BaseModel):
    id:int
    owner_id:int
    food_name:str
    category_id:int
    price:float
    due_date:dt
    comment:str
    is_anonymus:bool
    is_completed:bool
    is_trashed:bool
    