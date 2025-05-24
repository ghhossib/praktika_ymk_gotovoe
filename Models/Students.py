from Models.Base import *
from Models.Groups import Groups


class Students(Base):
    id = PrimaryKeyField()
    surename = CharField()
    name = CharField()
    middle_name = CharField()
    full_name_in_the_genitive_case = CharField()
    group_id = ForeignKeyField(Groups)
    specialization = CharField()
    date_of_birth = DateField()


    class Meta:
        table_name = 'students'

if __name__ == "__main__":
    pass