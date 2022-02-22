from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    if request.method == "POST":
        return redirect('/login', permanent=False)
    return render(request, "register.html")