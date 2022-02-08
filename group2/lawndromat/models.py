from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userTitle = models.TextChoices("Customer", "Worker")
    password = models.CharField(max_length=50)
    userPermission = models.CharField(max_length=10)
    money = models.IntegerField()
    
    
class test(models.Model):
    testName = models.CharField(max_length=50)
    testemail = models.CharField(max_length=50)