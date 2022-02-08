from atexit import register
from django.contrib import admin
from .models import test, User
# Register your models here.
admin.site.register(User)