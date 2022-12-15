from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def Home(request):
        if request.user.is_authenticated:
                print(request.user.username)
                return render(request, "Student/UserHome.html")
        else:
                return redirect('/login')