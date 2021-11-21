from typing import List
from pydantic import parse_obj_as

from .basic_handler import BasicHandler
from model.category import Category
from db.utils import unpack_category


class CategoryHandler(BasicHandler):
    INSERT_CATEGORY_QUERY = "INSERT INTO {} (category_name, avg_calories) VALUES(%s,%s)"

    def insert_category(self, args):
        self.execute(CategoryHandler.INSERT_CATEGORY_QUERY, args)
        category = self.select_category_by_name([args[0]])
        return category

    DELETE_CATEGORY_QUERY = "DELETE FROM {} WHERE category_name=%s"

    def delete_category_by_category_name(self, args):
        category = self.select_category_by_name(args)
        self.execute(CategoryHandler.DELETE_CATEGORY_QUERY, args)
        return category

    SELECT_CATEGORY_BY_NAME_QUERY = "SELECT * FROM {} WHERE category_name=%s"

    def select_category_by_name(self, args)->Category:
        result = self.execute(CategoryHandler.SELECT_CATEGORY_BY_NAME_QUERY, args)
        category = Category(**unpack_category(result[0]))
        return category
    
    SELECT_CATEGORY_ALL_QUERY = "SELECT * FROM {}"
    def select_all_category(self) -> List[Category]:
        result = self.execute(CategoryHandler.SELECT_CATEGORY_ALL_QUERY, [])
        category_list = list()
        for row in result:
            category_list.append(Category(**unpack_category(row)))
        if len(category_list)==0:
            raise IndexError
        return parse_obj_as(List[Category], category_list)
