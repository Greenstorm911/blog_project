from blog.models import articale, Category

def last_articale(request):
    last = articale.objects.last()
    return {"last_article" : last}
def recent(request):
    recent_article = articale.objects.all().order_by('-date')[0:3]
    categorys = Category.objects.all()
    return {'recents':recent_article, 'categorys' : categorys}