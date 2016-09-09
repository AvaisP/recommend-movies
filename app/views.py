from django.shortcuts import render
from django.http import HttpResponse
import os,re
from .models import Greeting,User,Movie,Rating

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    run_once()
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def run_once():
    pass