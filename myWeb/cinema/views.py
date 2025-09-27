from django.shortcuts import render, get_object_or_404
from .models import Movie, Reviewer

def index(request):
    movies = Movie.objects.all().prefetch_related('genres', 'review_set')
    return render(request, 'index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(
        Movie.objects.prefetch_related('genres', 'review_set__reviewer'),
        id=movie_id
    )
    return render(request, 'movie_detail.html', {'movie': movie})

def reviewer_detail(request, reviewer_id):
    reviewer = get_object_or_404(
        Reviewer.objects.prefetch_related('review_set__movie'),
        id=reviewer_id
    )
    return render(request, 'movies/reviewer_detail.html', {'reviewer': reviewer})