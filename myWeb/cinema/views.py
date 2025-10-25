from django.shortcuts import render
from .models import Movie, Reviewer

def index(request):
    movies = Movie.objects.all().prefetch_related('genres', 'review_set')
    return render(request, 'index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.prefetch_related('genres', 'review_set__reviewer').get(id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def reviewer_detail(request, reviewer_id):
    reviewer = Reviewer.objects.prefetch_related('review_set__movie').get(id=reviewer_id)
    return render(request, 'reviewer_detail.html', {'reviewer': reviewer})