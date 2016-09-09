from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting,User,Movie,Rating,cluster
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def cluster(request):
    all_user_id = map(lambda x : x.userid, User.objects.all())
    all_movie_id = set(map(lambda x:x.movieid, Movie.objects.all())