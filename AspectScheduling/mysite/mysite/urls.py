"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.template import loader
import os
import  sys
def MainPage(request):
    with open(os.path.join(sys.path[0], "mysite\Main.html"), "r") as f:
        return HttpResponse(f.read())


urlpatterns = [
    path('', MainPage),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
