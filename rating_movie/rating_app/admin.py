from django.contrib import admin
from rating_app.models import Movie

# Register your models here.
from django.contrib.auth.models import User

admin.site.register(Movie)
# admin.site.unregister(User)