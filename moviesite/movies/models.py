from django.db import models
from datetime import datetime


class Director(models.Model):
    director_name = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.director_name


class Rating(models.Model):
    rating_name = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ["rating_name"]

    def __str__(self) -> str:
        return self.rating_name


# Create your models here.


class Movie(models.Model):
    movie_title = models.CharField(max_length=200, blank=False)
    date_watched = models.DateTimeField("date watched")
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    media_name = models.CharField(max_length=32, null=True)

    def __str__(self) -> str:
        return self.movie_title


class Actor(models.Model):
    actor_name = models.CharField(max_length=32, unique=True)
    actors = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.actor_name
