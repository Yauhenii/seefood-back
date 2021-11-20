from .basic_handler import BasicHandler


class UserHandler(BasicHandler):
    INSERT_USER_QUERY = (
        "INSERT INTO {} (login_name, full_name, address_name, phone_number) VALUES(%s,%s,%s,%s)"
    )

    def insert_user(self, args):
        self.execute(UserHandler.INSERT_USER_QUERY, args)

    DELETE_USER_QUERY = "DELETE FROM {} WHERE login_name=%s"

    def delete_user_by_login(self, args):
        self.execute(UserHandler.DELETE_USER_QUERY, args)

    SELECT_USER_QUERY = "SELECT * FROM {} WHERE login_name=%s"

    def select_user_by_login(self, args):
        result = self.execute(UserHandler.SELECT_USER_QUERY, args)
        return result
