from django.shortcuts import redirect, render
from .models import UserProfile, Request
from django.contrib.auth.models import User
import hashlib
import os
# Create your views here.

def register(request):
    if request.method == "POST":
        user1 = User.objects.create_user(username = request.POST["email"],
                                         email = request.POST["email"],
                                         password = request.POST["password"])
        profile = UserProfile(user=user1,
                              userName = request.POST["name"],
                              userZipCode = request.POST["zipcode"],
                              userAddress = request.POST["address"],
                              userType = request.POST["type"],
                              money = 0)
        user1.save()
        profile.save()
        return redirect('/', permanent=False)
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        # Check if user info is valid
        pass
    return render(request, 'login.html')

def index(request):
    return redirect('login/', permanent=False)
