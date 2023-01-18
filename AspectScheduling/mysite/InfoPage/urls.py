
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from . import views

def Redirect(request):
    return redirect('/main')

urlpatterns = [
    path('logout', views.Logout),
    path('main', views.Main),
    path('login', views.Login),
    path('', Redirect),
]
