from Models.College import *


class CollegeController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return College.select()



    @classmethod
    def show(cls, id):
        return College.get_or_none(id)

if __name__ == "__main__":
    pass