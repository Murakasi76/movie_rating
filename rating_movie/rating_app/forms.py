from django import forms
from rating_app.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        modele = Movie
        fields = ["title", "genre", "release_date", "rating"]
