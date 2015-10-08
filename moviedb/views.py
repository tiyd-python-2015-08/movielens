from django.shortcuts import render
from .models import Movie
# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'moviedb/movie_detail.html',
                  {'movie': movie})
