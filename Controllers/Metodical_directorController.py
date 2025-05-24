from Models.Metodical_director import *


class Metodical_directorController:
    # метод вывода всех записей таблицы статусы
    @classmethod
    def get(cls):
        return Metodical_director.select()



    @classmethod
    def show(cls, id):
        return Metodical_director.get_or_none(id)


    @classmethod
    def add(cls, surename, name, middle_name, initials, role_id):
        Metodical_director.create(surename=surename,
                                  name=name,
                                  middle_name=middle_name,
                                  initials=initials,
                                  role_id=role_id)


    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Metodical_director.update({key: value}).where(Metodical_director.id == id).execute()


    @classmethod
    def delete(cls, id):
        Metodical_director.delete_by_id(id)


if __name__ == "__main__":
    pass
