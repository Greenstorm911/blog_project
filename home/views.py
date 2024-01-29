from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
def home(request):
    return render(request, "home/index.html")

def logout_founction(request):
    logout(request)
    return redirect('/')
