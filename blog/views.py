from django.shortcuts import render
from .models import articale
def detail(request, pk):
    
    return render(request, "blog/post-details.html")
