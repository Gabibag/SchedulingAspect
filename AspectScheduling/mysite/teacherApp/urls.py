from django.urls import include, path
from . import views
urlpatterns = [
    path('home', views.Home),
    path('create', views.CreateClass)
]
