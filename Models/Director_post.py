from Models.Base import *

class Director_post(Base):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        table_name = 'director_post'

if __name__ == "__main__":
    pass