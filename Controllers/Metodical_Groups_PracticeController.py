from Models.Metodical_Groups_Practice import *


class CollegeController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return Metodical_Groups_Practice.select()



    @classmethod
    def show(cls, id):
        return Metodical_Groups_Practice.get_or_none(id)

if __name__ == "__main__":
    pass