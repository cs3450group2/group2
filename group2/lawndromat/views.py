from django.shortcuts import redirect, render
from .models import User, Request
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
        user = User.objects.create(userZipCode = request.POST["zipcode"],
                                        userAddress = request.POST["address"],
                                        userName = request.POST["name"],
                                        email = request.POST["email"],
                                        userType = request.POST["type"],
                                        password = hPasword,
                                        money=0)
        user.save()        
        return redirect('/', permanent=False)
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        # Check if user info is valid
        pass
    return render(request, 'login.html')

def index(request):
    return redirect('login/', permanent=False)