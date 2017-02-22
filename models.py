from peewee import *
from database import Database

class Story(Model):
    title=CharField(default="Title")
    text=CharField(default="User story")
    criteria=CharField(default="Acceptance criteria")
    value=IntegerField(default=100)
    estimation=FloatField(default=1.0)
    status=CharField(default="Status")
    class Meta:
        database=Database.database

