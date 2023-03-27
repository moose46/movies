from django.db import models
from datetime import datetime


class Director(models.Model):
    director_name = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.director_name


class Genres(models.Model):
    genre = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self) -> str:
        return self.genre


class Rating(models.Model):
    rating_name = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ["rating_name"]

    def __str__(self) -> str:
        return self.rating_name


# Create your models here.


class Movie(models.Model):
    movie_title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=512)
    date_watched = models.DateTimeField("date watched")
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    media_name = models.CharField(max_length=32, null=True)

    def __str__(self) -> str:
        return self.movie_title


# class Movie2(Movie):
#     pass


class Actor(models.Model):
    actor_name = models.CharField(max_length=32, unique=True)
    actors = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.actor_name
