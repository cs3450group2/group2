from cProfile import Profile
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
        return redirect('/request/', permanent=False)
    else:
        return render(request, 'homepage.html')

@login_required
def newrequest(request):
    if request.user.userprofile.userType == "worker":
        return redirect('/request/', permanent=False)
    if request.method == "POST":
        req = Request.objects.create(requestZip = request.user.userprofile.userZipCode,
                                     customerID = request.user.id,
                                     type = request.POST['type'],
                                     date = request.POST['date'],
                                     timeOfDay = request.POST['timeofday'],
                                     cost = 10)
        req.save()
        return redirect('/request/', permanent=False)
    return render(request, "newrequest.html")

@login_required
def requests(request):
    if request.user.userprofile.userType == "customer" or "owner":
        requests = Request.objects.filter(customerID=request.user.id, complete=False).all()
        for r in requests:
            if r.workerID is not None:
                r.worker = User.objects.get(id=r.workerID)
    else:
        requests = Request.objects.filter(workerID=request.user.id, complete=False).all()
        for r in requests:
            r.customer = User.objects.get(id=r.customerID)
            r.cost = r.cost * 0.95
    for r in requests:
        if r.type == "lawn":
            r.typeFormatted = "Lawn Mowing"
        elif r.type == "rake":
            r.typeFormatted = "Leaf Raking"
        else:
            r.typeFormatted = "Snow Shoveling"
        
        r.timeOfDayFormatted = r.timeOfDay.capitalize()
    return render(request, 'requests.html', {'requests':requests, 'title':'My Jobs'})

@login_required
def pastRequests(request):
    if request.user.userprofile.userType == "customer" or "owner":
        requests = Request.objects.filter(customerID=request.user.id, complete=True).all()
        for r in requests:
            if r.workerID is not None:
                r.worker = User.objects.get(id=r.workerID)
    else:
        requests = Request.objects.filter(workerID=request.user.id, complete=True).all()
        for r in requests:
            r.customer = User.objects.get(id=r.customerID)
            r.cost = r.cost * 0.95
    for r in requests:
        if r.type == "lawn":
            r.typeFormatted = "Lawn Mowing"
        elif r.type == "rake":
            r.typeFormatted = "Leaf Raking"
        else:
            r.typeFormatted = "Snow Shoveling"
        
        r.timeOfDayFormatted = r.timeOfDay.capitalize()
    return render(request, 'requests.html', {'requests':requests, 'title':'Completed Jobs'})

@login_required
def openRequests(request):
    if request.user.userprofile.userType == "customer":
        return redirect('/request/', permanent=False)
    if request.user.userprofile.availability == '':
        return render(request, 'requests.html', {'requests': [], 'title': 'Available Jobs'})
    availabilities = request.user.userprofile.availability.split(';')
    requests = []
    for availability in availabilities:
        day, timeOfDay = availability.split(',')
        requests += Request.objects.filter(requestZip=request.user.userprofile.userZipCode, timeOfDay=timeOfDay, date__week_day=int(day), workerID=None).all()
    for r in requests:
        r.customer = User.objects.get(id=r.customerID)
        r.cost = r.cost * 0.95
        if r.type == "lawn":
            r.typeFormatted = "Lawn Mowing"
        elif r.type == "rake":
            r.typeFormatted = "Leaf Raking"
        else:
            r.typeFormatted = "Snow Shoveling"
        r.timeOfDayFormatted = r.timeOfDay.capitalize()
    return render(request, 'requests.html', {'requests': requests, 'title': 'Available Jobs'})

@login_required
def request(request, id):
    if request.method == "POST":
        if request.POST['action'] == "accept":
            r = Request.objects.get(id=id)
            r.workerID = request.user.id
            r.save()
            return redirect('/request/', permanent=False)
        elif request.POST['action'] == "complete":
            r = Request.objects.get(id=id)
            #TODO: Transfer Money
            r.complete = True
            r.save()
            return redirect('/request/past', permanent=False)
        else:
            r = Request.objects.get(id=id)
            r.feedBack = "test"
            r.thumbsUp = True
            r.save()
            return redirect('/request/past', permanent=False)
    if request.user.userprofile.userType == "customer":
        r = Request.objects.get(id=id, customerID=request.user.id)
        if r.workerID is not None:
            r.worker = User.objects.get(id=r.workerID)
    elif request.user.userprofile.userType == "worker":
        r = Request.objects.get(id=id)
        if r.workerID is not None and r.workerID != request.user.id:
            return redirect('/request/', permanent=False)
        r.customer = User.objects.get(id=r.customerID)
        r.cost = r.cost * 0.95
    else:
        r = Request.objects.get(id=id)
    
    if r.type == "lawn":
        r.typeFormatted = "Lawn Mowing"
    elif r.type == "rake":
        r.typeFormatted = "Leaf Raking"
    else:
        r.typeFormatted = "Snow Shoveling"
    
    r.timeOfDayFormatted = r.timeOfDay.capitalize()

    return render(request, 'request.html', {'request': r})

@login_required
def profile(request):
    availabilities = request.user.userprofile.availability.split(';')
    aval = []
    print(availabilities)
    for availability in availabilities:
        timeOfDay = availability.split(',')
        if timeOfDay[0] == '2':
            aval.append(["Monday",timeOfDay[1]])
        elif timeOfDay[0] == '3':
            aval.append(["Tuesday",timeOfDay[1]])
        elif timeOfDay[0] == '4':
            aval.append(["Wednesday",timeOfDay[1]])
        elif timeOfDay[0] == '5':
            aval.append(["Thursday",timeOfDay[1]])
        elif timeOfDay[0] == '6':
            aval.append(["Friday",timeOfDay[1]])
        elif timeOfDay[0] == '7':
            aval.append(["Saturday",timeOfDay[1]])
        elif timeOfDay[0] == '1':
            aval.append(["Sunday",timeOfDay[1]])
        
        
       
    #     users += request.user.objects.filter(timeOfDay=timeOfDay).all()
    return render(request, "profile.html", {"availabilities": aval})

@login_required
def availability(request):
    if request.method == "POST":
        schedule = ";".join(request.POST.getlist("data"))
        request.user.userprofile.availability = schedule
        request.user.userprofile.save()
        return redirect('/accounts/profile/', permanent=False)
    return render(request, "availability.html")    

@login_required
def profileupdate(request):
    if request.method == "POST":
        if request.POST["email"]:
            request.user.email = request.POST["email"]
            request.user.username = request.POST["email"]
        if request.POST["name"]:
            request.user.userprofile.userName = request.POST["name"]
        if request.user.userprofile.userType == "customer" or "owner" and request.POST["address"]:
            request.user.userprofile.userAddress = request.POST["address"]
        if request.POST["zipcode"]:
            request.user.userprofile.userZipCode = request.POST["zipcode"]   
            
        request.user.save()
        request.user.userprofile.save()
        return redirect('/accounts/profile/', permanent=False)
    return render(request, "profileupdate.html")

@login_required
def money(request):
    if 'deposit' in request.POST:
        if (request.user.userprofile.userType == "customer" or "owner") and (float(request.POST["deposit"])) > 0:
            request.user.userprofile.money += float(request.POST["deposit"])
    if 'withdraw' in request.POST:
        if request.user.userprofile.money >= float(request.POST["withdraw"]) and float(request.POST["withdraw"]) > 0:
            request.user.userprofile.money -= float(request.POST["withdraw"])
    request.user.userprofile.save()
    return render(request, "managemoney.html")

    
@login_required
def userlist(request):
    if request.user.userprofile.userType != "owner":
        return redirect('/', permanent=False)
    else:
        users = User.objects.all()
        return render(request, "userlist.html", {'users':users})
