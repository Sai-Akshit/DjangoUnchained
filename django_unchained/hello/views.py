from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "hello/index.html")

def suresh(request):
    return HttpResponse("Hello, Suresh!")

def ramesh(request):
    return HttpResponse("Hello, Ramesh!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })