from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def greeting(request, name):
    return HttpResponse(f"<h1>Hello {name.capitalize()}!</h1>")