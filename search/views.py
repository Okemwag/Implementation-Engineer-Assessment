from django.shortcuts import render
from .models import Movie



def search(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'search/search_form.html',	{'searchTerm': searchTerm, 'movies': movies})






