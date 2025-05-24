from Models.Post import *

class PostController:
    #Метод вывода всех записей таблицы Роли
    @classmethod
    def get(cls):
        return Post.select()

    @classmethod
    def show(cls, id):
        return Post.get_or_none(id)

    #CRUD
    @classmethod
    def add(cls, name):
        Post.create(name=name)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Post.update({key: value}).where(Post.id == id).execute()

    @classmethod
    def delete(cls, id):
        Post.delete().where(Post.id == id).execute()
if __name__ == '__main__':
    #for row in PostController.get():
        #print(row.name)
    pass