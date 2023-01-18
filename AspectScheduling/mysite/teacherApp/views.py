from django.shortcuts import render, redirect
from .forms import CreateClassForm
from studentApp.models import SignUp

def Home(request):
    if request.user.is_authenticated:
        return render(request, "Teacher/Main.html", {
            'user': request.user,
        })
    else:
        return redirect("/main")
def CreateClass(request):
    if LoginAndTeacher(request):
        if not request.POST:
            context = {
                "user" : request.user,
                "form" : CreateClassForm()
            }
            return render(request, "Teacher/CreateClass.html",context=context)
        else:
            
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            context = {
                "user" : request.user,
                "form" : CreateClassForm()
            }
            try:
                c = SignUp(name = name, description = desc)
                c.save()
                context['status'] = 'created'
            except:
                context['status'] = 'failed'
            return render(request, "Teacher/CreateClass.html",context=context)

    else:
        return redirect("/login")

def LoginAndTeacher(req):
    return req.user.is_authenticated and req.user.Teacher