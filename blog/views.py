from django.shortcuts import render
from .models import articale
from django.shortcuts import get_object_or_404
def detail(request, slug):
    requested_articale = get_object_or_404(articale, slug=slug)
    recent_article = articale.objects.all().order_by('-date')[0:3]
    return render(request, "blog/post-details.html", context={'articale':requested_articale, 'recents':recent_article})
