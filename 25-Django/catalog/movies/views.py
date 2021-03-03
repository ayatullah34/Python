from django.shortcuts import render
from .models import Movie
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.

def index(request):
    movies = Movie.objects.all()

    context = {
        'movies' : movies
    }
    return render(request,'movies/list.html',context)

    
def detail(request,movie_id):
    # try:
    #     movies = Movie.objects.get(pk = movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404('aradığınız kayıt yoktur')

    movie = get_object_or_404(Movie,pk = movie_id)
    context = {
        'movie' : movie
    }

    #return render(request,'movies/detail.html',movie)
    return render(request,'movies/detail.html',context)


def search(request):
    return render(request,'movies/search.html')
