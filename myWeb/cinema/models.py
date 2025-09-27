from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre (models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie (models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre)

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            return round(sum(review.rating for review in reviews) / len(reviews), 1)

    def review_count(self):
        return self.review_set.count()

    def __str__(self):
        return self.name

class Reviewer (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review (models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    text = models.TextField()
    published_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"{self.reviewer.name} - {self.movie.title} ({self.rating}/10)"
