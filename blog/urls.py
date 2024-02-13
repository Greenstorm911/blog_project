from django.urls import path 
from . import views

app_name = 'blog'
urlpatterns = [
    path('detail/<str:slug>', views.detail, name="detail"),
    path('blogs', views.blogs, name="all"),
    path('category/<int:pk>',views.category_view, name="category")
]
