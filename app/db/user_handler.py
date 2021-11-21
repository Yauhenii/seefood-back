from typing import List
from pydantic import parse_obj_as

from model.user import User
from db.basic_handler import BasicHandler
from db.utils import unpack_user


class UserHandler(BasicHandler):
    INSERT_USER_QUERY = "INSERT INTO {} (login_name, full_name, address_name, phone_number) VALUES(%s,%s,%s,%s)"

    def insert_user(self, args) -> User:
        self.execute(UserHandler.INSERT_USER_QUERY, args)
        user = self.select_user_by_login([args[0]])
        return user

    DELETE_USER_QUERY = "DELETE FROM {} WHERE login_name=%s"

    def delete_user_by_login(self, args) -> User:
        user = self.select_user_by_login(args)
        self.execute(UserHandler.DELETE_USER_QUERY, args)
        return user

    SELECT_USER_BY_LOGIN_QUERY = "SELECT * FROM {} WHERE login_name=%s"

    def select_user_by_login(self, args) -> User:
        result = self.execute(UserHandler.SELECT_USER_BY_LOGIN_QUERY, args)
        user = User(**unpack_user(result[0]))
        return user

    SELECT_ALL_USER_QUERY = "SELECT * FROM {}"

    def select_all_user(self) -> List[User]:
        result = self.execute(UserHandler.SELECT_ALL_USER_QUERY, [])
        user_list = list()
        for row in result:
            user_list.append(User(**unpack_user(row)))
        if len(user_list)==0:
            raise IndexError
        return parse_obj_as(List[User], user_list)
