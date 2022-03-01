from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.

    
class User(models.Model):
    userZipCode = models.IntegerField()
    userAddress = models.CharField(max_length=100,default="")
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userType = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
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