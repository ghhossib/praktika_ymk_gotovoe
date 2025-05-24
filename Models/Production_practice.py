from Models.Base import *

class Production_practice(Base):
    id = PrimaryKeyField()
    practice_name = CharField()
    module_name = CharField()


    class Meta:
        table_name = 'production_practice'

if __name__ == "__main__":
    pass