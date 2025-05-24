from Models.Base import *
from Models.Post import Post


class Director(Base):
    id = PrimaryKeyField()
    surename = CharField()
    middle_name = CharField()
    full_name_in_the_genetive_case = TextField()
    initials = CharField()
    post_id = ForeignKeyField(Post)
    phone_number = CharField()
    name = CharField()

    class Meta:
        table_name = 'director'

if __name__ == "__main__":
    pass