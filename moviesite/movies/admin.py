from django.contrib import admin
from .models import Movie, Director, Actor, Rating, MovieActor


class ActorInLine(admin.TabularInline):
    model = Actor
    extra = 3


class MovieActorInLine(admin.TabularInline):
    model = MovieActor


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["movie_title", "rating"]}),
        (
            "Date Watched",
            {"fields": ["date_watched", "director"], "classes": ["collapse"]},
        ),
    ]

    inLines = [MovieActorInLine]
    list_display = ("movie_title", "rating")


class ActorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["actor_name"]}),
    ]

    list_display = ["actor_name"]


# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
