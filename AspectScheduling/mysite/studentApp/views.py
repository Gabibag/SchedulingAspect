from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from studentApp.models import SignUp

def Home(request):
        if LoginAndStudent(request):
                print(request.user.username)
                context = {
                        'user': request.user
                }
                return render(request, "Student/UserHome.html",context=context)
        else:
                return redirect('/login')

def Signup(request):
        if LoginAndStudent(request):
                context = {
                        'user': request.user
                }
                classes = SignUp.objects.all()
                #todo Filter
                context['classes'] = classes
                return render(request, "Student/Signup.html", context=context)
        else:
                return redirect('/login')


def Classes(request, id):
        if LoginAndStudent(request):
                c = get_object_or_404(SignUp, pk = id)
                context = {
                        "user" : request.user,
                        "class": c
                }
                return render(request, "Student/Class.html", context= context)
        else:
                return redirect("/login")
                

def LoginAndStudent(request):
        return request.user.is_authenticated and request.user.Student