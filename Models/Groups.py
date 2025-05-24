from Models.Base import *

class Groups(Base):
    id = PrimaryKeyField()
    name = CharField()
    course = CharField()

    class Meta:
        table_name = 'groups'

if __name__ == "__main__":
    pass