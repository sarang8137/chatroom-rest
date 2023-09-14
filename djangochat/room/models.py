from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)

class Message(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    date_added=models.DateTimeField(default=datetime.now,blank=True)
