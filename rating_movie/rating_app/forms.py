from django import forms
from rating_app.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "genre", "release_date", "rating"]
        widgets = {
            "release_date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "title": forms.TextInput(attrs={"class": "content_title", "placeholder": "Enter book title "}),
            
        }
