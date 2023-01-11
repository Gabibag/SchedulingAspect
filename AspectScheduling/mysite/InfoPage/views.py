from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login,logout
    
def Main(request):
    template = loader.get_template("InfoPage/Main.html")
    context = {}
    return HttpResponse(template.render(context, request))
def Login(request):
    if request.POST:
        u = request.POST.get('login')
        p = request.POST.get('password')
        user = authenticate(request,username =  u,password = p)
        if not (user is None):
            login(request, user)
            return redirect('/studentApp/home')
        else:
            con = {'form': LoginForm(), 'error': 'incorrect login'}
            if User.objects.filter(username = u).exists():
                con['error'] = 'Invaild Password!'
            else:
                con['error'] = 'No user with that username exist'
            return HttpResponse(loader.get_template("InfoPage/Login.html").render(con, request))
    template = loader.get_template("InfoPage/Login.html")
    context = {}
    context['form'] = LoginForm()
    context['error'] = ''
    return HttpResponse(template.render(context, request))
def Logout(request):
    logout(request)
    return redirect('/')
