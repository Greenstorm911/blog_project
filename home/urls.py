from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    path('', views.home ,name="main"),
    path('logout', views.logout_founction, name="logout"),
]
