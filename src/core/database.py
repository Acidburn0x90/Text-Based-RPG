from peewee import *

db = SqliteDatabase('game.db')

class BaseModel(Model):
    class Meta:
        database = db

class Player(BaseModel):
    name = CharField()
    level = IntegerField(default=1)
    experience = IntegerField(default=0)
    hp = IntegerField(default=100)
    hpmax = IntegerField(default=100)
    money = IntegerField(default=25)
    location = TextField(default="N/A")