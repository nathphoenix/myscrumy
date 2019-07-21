# Create your views here.
from django.shortcuts import render
from .models import ScrumyGoals, Post, Comment, ScrumyHistory, GoalStatus
# Create your views here.
from django.http import HttpResponse
from random import randint
from django.contrib.auth.models import User


# def index(request):
#     return HttpResponse("<h1 style = 'font-size:30px' >Hello world.. Today is sunday</h1>")
def index(request):
    latest_goal_name = ScrumyGoals.objects.order_by('goal_name')[:4]
    output = ', '.join([q.goal_name for q in latest_goal_name])
    return HttpResponse(output)
def posts(request):
    return HttpResponse("<h1 style = 'font-size:30px' >Welcome to the post section</h1>")
def comments(request):
    return HttpResponse("<h1 style = 'font-size:30px' >Your comments are important to us!!!</h1>")

def movegoal(request, goal_id):
    if goal_id != 1:
        return HttpResponse("<h1 style = 'font-size:30px' >Welcome to the movegoal page...."
        "You are seeing this page because the id you entered is not available on the database</h1>")
    else:
        move = ScrumyGoals.objects.get(pk=1)
        return HttpResponse(move)


def add_goal(request, goal_name):
        
        status = GoalStatus.objects.get(status_name='Weekly Goal')
        user_ = User.objects.get(username='louis')
        added = ScrumyGoals(goal_name = 'Keep Learning Django', goal_id = randint(100, 999), created_by='Louis',
        moved_by='Louis', user = user_, goal_status=status, owner='Louis')
        added.save()
        return HttpResponse(added)

def home(request, goal_name):
    status = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    return HttpResponse(status)


# def detail(request, message):
#     return HttpResponse("<h1 style = 'font-size:30px' >You are looking at comment: %s </h1>" %message)
# def results(request, message):
#     return HttpResponse("<h1 style = 'font-size:30px' >You are looking the result page %s </h1>" %message)
# def vote(request, message):
  
#     response = "<h1 style = 'font-size:30px' >You are voting at question %s </h1>"
#     # response = "You are voting at question %s"
#     return HttpResponse( response % message)
