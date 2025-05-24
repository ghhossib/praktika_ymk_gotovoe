from Models.Base import *
from Models.Roles import Roles
from flask_login import UserMixin


class Users(UserMixin,Base):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    role_id = ForeignKeyField(Roles)

    class Meta:
        table_name = 'users'

if __name__ == "__main__":
    pass