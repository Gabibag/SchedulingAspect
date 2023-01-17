from django.urls import include, path
from . import views

urlpatterns = [
    path('home', views.Home),
    path('signup', views.Signup)
]
