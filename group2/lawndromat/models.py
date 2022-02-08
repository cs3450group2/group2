from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userType = models.TextChoices("Customer", "Worker")
    password = models.CharField(max_length=50)
    money = models.IntegerField()
    
    
