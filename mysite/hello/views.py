from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sayHello(request):
    html = "<h1> Hello, !! <h1>"
    return HttpResponse(html)