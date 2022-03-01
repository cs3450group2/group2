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
    userAddress = models.CharField(max_length=100)
    userType = models.CharField(max_length=50)
    money = models.FloatField(default=0)


class Request(models.Model):
    requestZip = models.IntegerField()
    customerID = models.IntegerField()
    date = models.DateTimeField()
    timeOfDay = models.CharField(max_length=50)
    workerID = models.IntegerField(default=None, null=True)
    complete = models.BooleanField(default=False)
    feedBack = models.TextField(default="")
    thumbsUp = models.BooleanField(default=None, null=True)
    cost = models.FloatField(default=0)
    type = models.CharField(max_length=10)
