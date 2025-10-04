from peewee import *

db = SqliteDatabase('game.db')

class BaseModel(Model):
    class Meta:
        database = db

class Player(BaseModel):
    name = CharField()
    level = IntegerField(default=1)
    experience = IntegerField(default=0)