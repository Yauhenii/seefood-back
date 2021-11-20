import psycopg2 as ps


class BasicHandler:
    host: str
    port: str
    user_name: str
    password: str
    table_name: str

    def __init__(
        self,
        host: str,
        port: str,
        user_name: str,
        password: str,
        table_name: str,
    ):
        self.host = host
        self.port = port
        self.user_name = user_name
        self.password = password
        self.table_name = table_name

    def execute(self, query, args):
        with ps.connect(
            host=self.host,
            port=self.port,
            user=self.user_name,
            password=self.password,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query.format(self.table_name), args)
                try:
                    result = cursor.fetchall()
                    connection.commit()
                    return result
                except ps.ProgrammingError:
                    connection.commit()
