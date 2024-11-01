from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login')
def index(request):
  return render(request, "index.html")

def Login(request):
  
  if request.method == "POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    if User.objects.filter(email=email).exists():
      user= User.objects.get(email=email)
      if user.check_password(password):
        if user is not None:
          login(request, user)
          return redirect("index")
        else:
          messages.warning(request, "Kullanıcı bulunamadı.")
      else:
        messages.warning(request, "Kullanıcı bulunamadı.")
  else:
    messages.warning(request, "eposta adı yada şifre hatalı")
      
  
  return render(request, "login.html")

def Logout(request):
  logout(request)
  return redirect('login')

def Register(request):
  
  if request.method == "POST":
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    username = request.POST.get("username")
    password = request.POST.get("password")

    if not User.objects.filter(username=username).exists():
      if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user.save()
        login(request, user)
        return redirect(f"/profile/{user.username}")
      else:
        messages.warning(request, "Bu E-posta adresi kullanılmaktadır.")
    else:    
      messages.warning(request, "Bu kullanıcı adı kullanılmaktadır.")
    
  return render(request, "register.html")

@login_required(login_url="/login")
def profile(request, username):
  try:
    profile = Profile.objects.get(user__username=username)
  except Profile.DoesNotExist:
    # Profil bulunamadıysa yapılacak işlemler
    return HttpResponse("Profil bulunamadı")
    
  context={
    "profile":profile
  }
  return render(request, "profile.html", context)
