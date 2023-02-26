from django.db import models
from datetime import datetime


class Ratings(models.IntegerChoices):
    BAD = 1
    GOOD = 2
    GREAT = 3
    AWFUL = 0


class Actor(models.Model):
    actor_name = models.CharField(max_length=200, null=False)


class Director(models.Model):
    director_name = models.CharField(max_length=200, null=False)


# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200, blank=False)
    date_watched = models.DateTimeField("date watched")
    rating = models.IntegerField(Ratings.choices, default=Ratings.GOOD)
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    media_name = models.CharField(max_length=32, null=True)
