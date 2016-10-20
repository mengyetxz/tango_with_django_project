from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    toAbout = "<br/> <a href='/rango/about'>About</a>"
    return HttpResponse("Rango says hey there world! %s" % toAbout)

def about(request):
    backToIndex = "<br/> <a href='/rango/'>Index</a>"
    return HttpResponse("Rango says here is the about page %s" % backToIndex)


