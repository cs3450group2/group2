from atexit import register
from django.contrib import admin
from .models import UserProfile, Request
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Request)