from django.urls import include, path
from . import views

urlpatterns = [
    path('home', views.Home),
    path('signup', views.Signup),
    path('signup/<int:id>', views.JoinClass),
    path('classes/<int:id>', views.Classes)
]
