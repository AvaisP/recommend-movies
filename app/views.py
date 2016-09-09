from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Greeting,User,Movie,Rating

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    run_once()
    return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def run_once():
    f = open("ml-100k/u.item", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('|', 24)
        if len(e) == 24:
            i.append(Item(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], \
            e[11], e[12], e[13], e[14], e[15], e[16], e[17], e[18], e[19], e[20], e[21], \
            e[22], e[23]))
    f.close()
    f = open("ml-100k/u.user", "r")
    print os.path
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('|', 5)
        if len(e) == 5:
            u.append(User.objects.create(e[0], e[1], e[2], e[3], e[4]))
    f.close()
    f = open("ml-100k/u.base", "r")
    text = f.read()
    entries = re.split("\n+", text)
    for entry in entries:
        e = entry.split('\t', 4)
        if len(e) == 4:
            r.append(Rating(e[0], e[1], e[2], e[3]))
    f.close()