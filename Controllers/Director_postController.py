from Models.Director_post import *


class Director_postController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return Director_post.select()



    @classmethod
    def show(cls, id):
        return Director_post.get_or_none(id)

if __name__ == "__main__":
    pass