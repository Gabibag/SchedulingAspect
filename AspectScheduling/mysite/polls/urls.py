#note: this was created not by default, had to manually make
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]