from Models.Students_director import *

class Students_directorController:
    #Метод вывода всех записей таблицы Роли
    @classmethod
    def get(cls):
        return Students_director.select()

    @classmethod
    def show(cls, id):
        return Students_director.get_or_none(id)

if __name__ == '__main__':
    for row in Students_directorController.get():
        print(row.id, row.surename, row.name, row.middle_name, row.initials, row.director_post_id)