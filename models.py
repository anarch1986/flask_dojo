from peewee import *


class CreateDatabase:

    def __init__(self):
        self.db = PostgresqlDatabase("flask_dojo", user="tomi")


class BaseModel(Model):

    class Meta:
        database = CreateDatabase().db


class Counter(BaseModel):
    get_counter = IntegerField()
    post_counter = IntegerField()
