from database import Database
from peewee import *

class Story(Model):
    title=CharField()
    text=CharField()
    criteria=CharField()
    value=IntegerField()
    estimation=FloatField()
    status=CharField()
    class Meta:
        database=Database.database

class CreateTables:
  def createtables():
    Database.database.drop_tables([Story],safe=True)
    Database.database.create_tables([Story],safe=True)