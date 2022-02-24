from statistics import mode
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.

    
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    userZipCode = models.IntegerField()
    userName = models.CharField(max_length=100)
    userAddress = models.CharField(max_length=100,default="")
    userType = models.CharField(max_length=50)
    money = models.IntegerField(default=0)


class Request(models.Model):
    requestID = models.IntegerField()
    requestZip = models.IntegerField()
    customerID = models.IntegerField()
    date = models.DateTimeField('date published')
    timeOfDay = CharField(max_length=50)
    workerID = models.IntegerField()
    complete = models.BooleanField(default=None)
    feedBack = models.TextField()
    thumbsUp = models.BooleanField(default=None)
    cost = models.IntegerField()
