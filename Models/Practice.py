from Models.Base import *
from Models.Director import Director
from Models.Production_practice import Production_practice


class Practice(Base):
    id = PrimaryKeyField
    organization = CharField()
    production_practice_id = ForeignKeyField(Production_practice)
    address = TextField()
    practice_time = CharField()
    start_date = DateField()
    end_date = DateField()
    director_id = ForeignKeyField(Director)



    class Meta:
        table_name = 'practice'

if __name__ == "__main__":
    pass