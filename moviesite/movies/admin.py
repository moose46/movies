from django.contrib import admin
from .models import Movie, Director, Actor, Rating, Genres


class ActorInLine(admin.TabularInline):
    model = Actor
    extra = 0


class GenreInLine(admin.TabularInline):
    model = Genres
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["movie_title", "rating", "genre"]}),
        (
            "Date Watched",
            {
                "fields": ["description", "date_watched", "director"],
                "classes": ["collapse"],
            },
        ),
    ]
    inlines = [ActorInLine]
    list_display = ("movie_title", "rating", "date_watched")


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
admin.site.register(Genres)
