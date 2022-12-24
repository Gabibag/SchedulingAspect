from django.shortcuts import render, redirect

def Home(request):
    if request.user.is_authenticated:
        return render(request, "Teacher/Main.html", {
            'user': request.user,
        })
    else:
        return redirect("/main")
def CreateClass(request):
    pass #TODO