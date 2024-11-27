from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib.auth import authenticate
from django.contrib.auth import logout

def index(request):
    if request.user.is_anonymous:
        return redirect(request,"login.html")
    else:
        return HttpResponse("this is homepage")

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]
        
        contact = Contact(name=name, username=username, password=password)
        contact.save();
        
        return render(request, "contact.html")
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("/")
        
        else:
            return render(request,"login.html")
    
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("login.html")
    
