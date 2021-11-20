from datetime import datetime as dt

from model.user import User
from model.order import Order


order_stub_1=Order(
    owner_name='John',
    food_name='Tomato',
    category_name='Vegetable',
    price='10',
    due_date=dt(2021,11,22),
    comment='1',
    is_anonymus=True,
    is_completed=False,
    is_trashed=False)

order_stub_2=Order(
    owner_name='Henry',
    food_name='Sausage',
    category_name='Meat',
    price='20',
    due_date=dt(2021,11,23),
    comment='Pork and beef',
    is_anonymus=False,
    is_completed=False,
    is_trashed=False)

user_stub_1=User(
    full_name='John',
    address='Somewherestr. 10',
    phone_number='01631133224'
)

class DBHandler:
    def get_all_orders(self):
        return [order_stub_1,order_stub_2]
    
    def get_all_users(self):
        return [user_stub_1]

