from django.contrib import admin
from rating_app.models import Movie
from rating_app.forms import MovieForm

# Register your models here.
from django.contrib.auth.models import User

# admin.site.register(Movie)
# admin.site.unregister(User)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    form = MovieForm
    # list_display = ("title", "genre", "release_date", "rating",)
    list_filter = ("genre", "release_date",)
    search_fields = ("title__startswith",)
    ordering = ("-release_date",)