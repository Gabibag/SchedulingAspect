
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from . import views

def Redirect(request):
    return redirect('/Main')

urlpatterns = [
    path('Main', views.Main),
    path('Login', views.Login),
    path('', Redirect),
]
