from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Movie



def search(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'search/search_form.html',	{'searchTerm': searchTerm, 'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'search/detail.html',
                  {'movie': movie, 'reviews': reviews})





