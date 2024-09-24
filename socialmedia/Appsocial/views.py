from django.shortcuts import render
from django.contrib.auth.models import User

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
    
    if not User.object.filter(user_name=user_name).exist():
      if not User.object.filter(email=email).exist():
        user = User.objects.create_user(
          first_name=first_name,
          last_name=last_name,
          email=email,
          user=user,
          password=password
        )
        
        user.save()
    
  return render(request, "register.html")

def Profile(request):
  return render(request, "profile.html")
