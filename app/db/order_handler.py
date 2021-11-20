import psycopg2 as ps

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

    def execute(self, query, args):
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

    INSERT_ORDER_QUERY = """INSERT INTO {} 
        (owner_id, food_name, category_id, price, due_date, comment, is_anonymus, is_completed, is_trashed) 
        VALUES((SELECT id from {} WHERE login_name=%s),%s,(SELECT id from {} WHERE category_name=%s),%s,%s,%s,%s,%s,%s);"""

    def insert_order_by_user_name_and_category(self, args):
        self.execute(OrderHandler.INSERT_ORDER_QUERY, args)
