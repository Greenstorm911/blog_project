from django.shortcuts import render
from .models import articale, Category
from django.shortcuts import get_object_or_404
def detail(request, slug):
    requested_articale = get_object_or_404(articale, slug=slug)
    return render(request, "blog/post-details.html", context={'articale':requested_articale})


def blogs(request):
    all_blogs = articale.objects.all()
    return render(request, "blog/blog.html", context={"blogs": all_blogs})


def category_view(request, pk):
    requested_category = get_object_or_404(Category, id=pk)
    posts = requested_category.articale_set.all()
    return render(request, "blog/blog.html", context={"blogs": posts})