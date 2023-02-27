from django.db import models
from datetime import datetime


class Ratings(models.IntegerChoices):
    BAD = 1
    GOOD = 2
    GREAT = 3
    AWFUL = 0


class Director(models.Model):
    director_name = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.director_name


class Rating(models.Model):
    rating_name = models.CharField(max_length=32)

    class Meta:
        ordering = ["rating_name"]

    def __str__(self) -> str:
        return self.rating_name


# Create your models here.
class Actor(models.Model):
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.actor_name


class Movie(models.Model):
    movie_title = models.CharField(max_length=200, blank=False)
    date_watched = models.DateTimeField("date watched")
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    # actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    media_name = models.CharField(max_length=32, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self) -> str:
        return self.movie_title


class MovieActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32)
