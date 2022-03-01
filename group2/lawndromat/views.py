from django.shortcuts import redirect, render
from .models import UserProfile, Request
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

def index(request):
    if request.user.is_authenticated:
        return redirect('accounts/profile/', permanent=False)
    else:
        return redirect('accounts/login/', permanent=False)

@login_required
def profile(request):
    return render(request, "profile.html")
