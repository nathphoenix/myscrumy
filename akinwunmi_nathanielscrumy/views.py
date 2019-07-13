# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style = 'font-size:30px' >Hello world.. Thank you for coming</h1>")
def posts(request):
    return HttpResponse("<h1 style = 'font-size:30px' >Welcome to the post section</h1>")
def comments(request):
    return HttpResponse("<h1 style = 'font-size:30px' >Your comments are important to us!!!</h1>")