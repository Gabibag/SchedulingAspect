from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from studentApp.models import SignUp

def Home(request):
        if request.user.is_authenticated:
                print(request.user.username)
                context = {
                        'user': request.user
                }
                return render(request, "Student/UserHome.html",context=context)
        else:
                return redirect('/login')

def Signup(request):
        if request.user.is_authenticated:
                context = {
                        'user': request.user
                }
                classes = SignUp.objects.all()
                #todo Filter
                context['classes'] = classes
                return render(request, "Student/Signup.html", context=context)
        else:
                return redirect('/login')