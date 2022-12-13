from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def Home(request):
        if request.user.is_authenticated:
                print("ok")
                return render(request, "Student/UserHome.html")
        else:
                redirect('/')