from pydantic import BaseModel
from datetime import datetime as dt


class Order(BaseModel):
    owner_name:str
    food_name:str
    category_name:str
    price:float
    due_date:dt
    comment:str
    is_anonymus:bool
    is_completed:bool
    is_trashed:bool
    