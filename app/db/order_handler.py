from typing import List
import psycopg2 as ps
from pydantic.tools import parse_obj_as

from db.utils import unpack_order
from model.order import Order
from .basic_handler import BasicHandler


class OrderHandler(BasicHandler):
    table_user_name: str
    table_category_name: str

    def __init__(
        self,
        host: str,
        port: str,
        user_name: str,
        password: str,
        table_name: str,
        table_user_name: str,
        table_category_name: str,
    ):
        super().__init__(host, port, user_name, password, table_name)
        self.table_user_name = table_user_name
        self.table_category_name = table_category_name

    def execute_three_tables(self, query, args):
        with ps.connect(
            host=self.host,
            port=self.port,
            user=self.user_name,
            password=self.password,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query.format(
                        self.table_name,
                        self.table_user_name,
                        self.table_category_name,
                    ),
                    args,
                )
                try:
                    result = cursor.fetchall()
                    connection.commit()
                    return result
                except ps.ProgrammingError:
                    connection.commit()

    INSERT_ORDER_BY_OWNER_AND_CATEGORY_NAME_QUERY = """INSERT INTO {}
        (owner_id, food_name, category_id, price, due_date, comment, is_anonymus, is_completed, is_trashed)
        VALUES((SELECT id from {} WHERE login_name=%s),%s,(SELECT id from {} WHERE category_name=%s),%s,%s,%s,%s,%s,%s);"""

    def insert_order_by_login_name_and_category(self, args):
        self.execute_three_tables(
            OrderHandler.INSERT_ORDER_BY_OWNER_AND_CATEGORY_NAME_QUERY, args
        )

    # INSERT_ORDER_BY_OWNER_AND_CATRGORY_ID_QUERY = """INSERT INTO {}
    # (owner_id, food_name, category_id, price, due_date, comment, is_anonymus, is_completed, is_trashed)
    # VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

    # def insert_order_by_user_name_and_category(self, args):
    #     self.execute(OrderHandler.INSERT_ORDER_QUERY, args)

    SELECT_ORDER_BY_ID_QUERY = "SELECT * FROM {} WHERE id=%s"

    def select_order_by_id(self, args) -> Order:
        result = self.execute(OrderHandler.SELECT_ORDER_BY_ID_QUERY, args)
        order = Order(**unpack_order(result[0]))
        return order

    SELECT_ALL_ORDER_QUERY = "SELECT * FROM {}"

    def select_all_order(self) -> List[Order]:
        result = self.execute(OrderHandler.SELECT_ALL_ORDER_QUERY, [])
        order_list = list()
        for row in result:
            order_list.append(Order(**unpack_order(row)))
        if len(order_list) == 0:
            raise IndexError
        return parse_obj_as(List[Order], order_list)

    DELETE_ORDER_BY_ID_QUERY = "DELETE FROM {} WHERE id=%s"

    def delete_order_by_id(self, args) -> Order:
        order = self.select_order_by_id(args)
        self.execute(OrderHandler.DELETE_ORDER_BY_ID_QUERY, args)
        return order
