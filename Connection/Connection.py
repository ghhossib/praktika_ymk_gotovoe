from peewee import *
#функция подключения к БД
def connect():
    mysql_db = MySQLDatabase('StaN1234_Project_x',
                             user='StaN1234_clients',
                             password='111111',
                             host='10.11.13.118',
                             port=3306)
    return mysql_db

if __name__ == "__main__":
    print(connect().connect())