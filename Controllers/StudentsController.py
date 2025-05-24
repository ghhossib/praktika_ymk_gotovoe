from Models.Students import *



class StudentsController:
    #Метод вывода всех записей таблицы Роли
    @classmethod
    def get(cls):
        return Students.select()

    @classmethod
    def show(cls, id):
        return Students.get(Students.id == id)

    @classmethod
    def show_group(cls, group_id):
        return Students.select().where(Students.group_id == group_id)

    #CRUD
    @classmethod
    def add(cls, surename, name, middle_name, full_name_in_the_genitive_case, group_id, specialization, date_of_birth):
        Students.create(surename=surename,
                    name=name,
                    middle_name=middle_name,
                    full_name_in_the_genitive_case=full_name_in_the_genitive_case,
                    group_id=group_id,
                    specialization=specialization,
                    date_of_birth=date_of_birth)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Students.update({key: value}).where(Students.id == id).execute()

    @classmethod
    def delete(cls, id):
        Students.delete().where(Students.id == id).execute()
if __name__ == '__main__':
   for row in StudentsController.show_group(5):
        print(row.id, row.surename, row.name, row.middle_name, row.full_name_in_the_genitive_case, row.group_id, row.specialization, row.date_of_birth)
