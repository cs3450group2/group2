from django.shortcuts import get_object_or_404, redirect, render
from .models import User, Request
from django import forms
import json
import hashlib
import os
# Create your views here.

def register(request):
    if request.method == "POST":
        salt = os.urandom(32)
        hPasword = hashlib.pbkdf2_hmac('sha256',
                                       request.POST["password"].encode("utf-8"),
                                       salt,
                                       100000,
                                       dklen=128)
        user = User.objects.create(userID = 1,
                                        userZipCode = request.POST["zipcode"],
                                        userName = request.POST["name"],
                                        email = request.POST["email"],
                                        userType = request.POST["type"],
                                        password = hPasword,
                                        money=0)
        user.save()        
        return redirect('/', permanent=False)
    return render(request, "register.html")

def login(request):
    return render(request, 'login.html')

def index(request):
    return redirect('login/', permanent=False)