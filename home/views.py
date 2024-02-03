from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from blog.models import articale, Category
def home(request):
    articales = articale.objects.all()
    # articales = articale.objects.filter(category=2)
    return render(request, "home/index.html", context={'articales' : articales})

def logout_founction(request):
    logout(request)
    return redirect('home:main')
