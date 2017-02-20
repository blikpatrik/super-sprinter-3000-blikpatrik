from peewee import *
from database import Database

class Story(Model):
    title=CharField(default="Title")
    text=CharField(default="User story")
    criteria=CharField(default="Acceptance criteria")
    value=IntegerField(default="Busines value")
    estimation=FloatField(default="Estimation")
    status=CharField(default="Status")
    class Meta:
        database=Database.database

class CreateTables:
  def createtables():
    Database.database.drop_tables([Story],safe=True)
    Database.database.create_tables([Story],safe=True)

