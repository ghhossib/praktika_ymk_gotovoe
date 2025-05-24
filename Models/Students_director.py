from Models.Base import *
from Models.Director_post import Director_post


class Students_director(Base):
    id = PrimaryKeyField()
    surename = CharField()
    name = CharField()
    middle_name = CharField()
    initials = CharField()
    director_post_id = ForeignKeyField(Director_post)

    class Meta:
        table_name = 'students_director'

if __name__ == "__main__":
    pass