from Models.Base import *
from Models.Roles import Roles


class Metodical_director(Base):
    id = PrimaryKeyField()
    surename = CharField()
    name = CharField()
    middle_name = CharField()
    initials = CharField()
    role_id = ForeignKeyField(Roles)


    class Meta:
        table_name = 'metodical_director'

if __name__ == "__main__":
    pass