from Models.Base import *
from Models.Groups import Groups
from Models.Metodical_director import Metodical_director
from Models.Practice import Practice


class Metodical_Groups_Practice(Base):
    id = PrimaryKeyField()
    metodical_director_id = ForeignKeyField(Metodical_director)
    group_id = ForeignKeyField(Groups)
    practice_id = ForeignKeyField(Practice)


    class Meta:
        table_name = 'metodical_Groups_Practice'

if __name__ == "__main__":
    pass