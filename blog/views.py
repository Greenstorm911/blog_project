from django.shortcuts import render
from .models import articale
from django.shortcuts import get_object_or_404
def detail(request, pk):
    requested_articale = get_object_or_404(articale, pk=pk)
    return render(request, "blog/post-details.html", context={'articale':requested_articale})
