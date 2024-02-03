from django.shortcuts import render
from .models import 
def detail(request, pk):
    
    return render(request, "blog/post-details.html")
