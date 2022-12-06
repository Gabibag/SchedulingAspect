from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def Main(request):
    template = loader.get_template("InfoPage/Main.html")
    context = {}
    return HttpResponse(template.render(context, request))