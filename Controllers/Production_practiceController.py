from Models.Production_practice import *

class Production_practiceController:
    #Метод вывода всех записей таблицы Роли
    @classmethod
    def get(cls):
        return Production_practice.select()

    @classmethod
    def show(cls, id):
        return Production_practice.get_or_none(id)

    #CRUD
    @classmethod
    def add(cls, practice_name, module_name):
        Production_practice.create(practice_name=practice_name,
                    module_name=module_name)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Production_practice.update({key: value}).where(Production_practice.id == id).execute()

    @classmethod
    def delete(cls, id):
        Production_practice.delete().where(Production_practice.id == id).execute()
if __name__ == '__main__':
    #for row in Production_practiceController.get():
        #print(row.id, row.practice_name, row.module_name)
    pass