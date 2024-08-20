from django.shortcuts import render

def index(request):
  return render(request, "index.html")

def Login(request):
  return render(request, "login.html")

def Register(request):
  return render(request, "register.html")

def Profile(request):
  return render(request, "profile.html")
