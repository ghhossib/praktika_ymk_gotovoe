from Models.Base import *
from Models.Groups import Groups
from Models.Students_director import Students_director


class College(Base):
    id = PrimaryKeyField()
    groups_id = ForeignKeyField(Groups)
    students_director_id = ForeignKeyField(Students_director)
    name = CharField()

    class Meta:
        table_name = 'college'

if __name__ == "__main__":
    pass