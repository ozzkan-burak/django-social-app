from django.shortcuts import render

def index(request):
  return render(request, "index.html")

def Login(request):
  return render(request, "login.html")

def Register(request):
  
  if request.method == "POST":
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    email=request.POST.get("email")
    user_name=request.POST.get("user_name")
    password=request.POST.get("password")
    
  return render(request, "register.html")

def Profile(request):
  return render(request, "profile.html")
