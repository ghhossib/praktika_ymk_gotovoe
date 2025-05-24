from Models.Practice import *

class PracticeController:
    #Метод вывода всех записей таблицы Роли
    @classmethod
    def get(cls):
        return Practice.select()

    @classmethod
    def show(cls, id):
        return Practice.get_or_none(id)

    #CRUD
    @classmethod
    def add(cls, organization, production_practice_id, address, practice_time, start_date, end_date, director_id):
        Practice.create(organization=organization,
                    production_practice_id=production_practice_id,
                    address=address,
                    practice_time=practice_time,
                    start_date=start_date,
                    end_date=end_date,
                    director_id=director_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Practice.update({key: value}).where(Practice.id == id).execute()

    @classmethod
    def delete(cls, id):
        Practice.delete().where(Practice.id == id).execute()
if __name__ == '__main__':
    #for row in PracticeController.get():
        #print(row.id, row.organization, row.production_practice_id, row.address, row.practice_time, row.start_date, row.end_date, row.director_id)
        pass