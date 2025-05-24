from Models.Base import *

class Files_Practice(Base):  # Лучше использовать BaseModel, если у вас такой есть
    name = CharField(max_length=100)
    file_data = BlobField()

    class Meta:
        table_name = 'files_practice'

if __name__ == "__main__":
    pass