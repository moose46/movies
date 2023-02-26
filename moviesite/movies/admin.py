from django.contrib import admin
from .models import Movie, Director, Actor


class ChoiceInLine(admin.StackedInline):
    model = Actor
    extra = 3


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["movie_title", "actors"]}),
        (
            "Date Watched",
            {"fields": ["date_watched", "director"], "classes": ["collapse"]},
        ),
    ]
    inLines = [ChoiceInLine]
    list_display = ("movie_title", "date_watched", "actors")


class ActorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["actor_name"]}),
    ]

    list_display = ["actor_name"]


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Actor, ActorAdmin)
