from Models.Director import *


class DirectorController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return Director.select()



    @classmethod
    def show(cls, id):
        return Director.get_or_none(id)

if __name__ == "__main__":
    pass