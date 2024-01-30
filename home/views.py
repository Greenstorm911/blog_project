from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from blog.models import articale
def home(request):
    articales = articale.objects.all()
    return render(request, "home/index.html", context={'articales' : articales})

def logout_founction(request):
    logout(request)
    return redirect('/')
