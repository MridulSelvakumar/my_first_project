from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def face(request):
    return HttpResponse("<h1><marquee>HI I AM DEVELOPER IN PYTHON</marquee></h1>")
