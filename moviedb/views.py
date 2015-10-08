from django.shortcuts import render
from django.db.models import Avg, Count

from .models import Movie, Rater


# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'moviedb/movie_detail.html',
                  {'movie': movie})


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    movie_ratings = []
    for rating in rater.rating_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'stars': '\u2605' * rating.stars,
        })
    return render(request,
                  'moviedb/rater_detail.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})


def top_movies(request):
    # movie_list = []
    # for movie in Movie.objects.all():
    #     if type(movie.average_rating()) == float:
    #         movie_list.append(movie)

    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'moviedb/top_movies.html',
                  {'movies': movies})
