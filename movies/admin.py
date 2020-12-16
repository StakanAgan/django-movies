from django.contrib import admin
from .models import (Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Reviews)

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
# Register your models here.
