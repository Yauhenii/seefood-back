from .basic_handler import BasicHandler


class CategoryHandler(BasicHandler):
    INSERT_CATEGORY_QUERY = "INSERT INTO {} (category_name, avg_calories) VALUES(%s,%s)"

    def insert_category(self, args):
        self.execute(CategoryHandler.INSERT_CATEGORY_QUERY, args)

    DELETE_CATEGORY_QUERY = "DELETE FROM {} WHERE category_name=%s"

    def delete_category_by_category_name(self, args):
        self.execute(CategoryHandler.DELETE_CATEGORY_QUERY, args)
