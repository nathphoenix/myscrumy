# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style = 'background-color:red, color: white, font-size:60px' >Hello world.. Thank you for coming</h1>")