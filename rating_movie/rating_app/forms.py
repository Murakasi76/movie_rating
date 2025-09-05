from django import forms
from rating_app.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "genre", "release_date", "rating"]
        widgets = {
            "release_date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "title": forms.Textarea(attrs={"class": "content_title", "placeholder": "Enter book title ", "rows": 3}),
            "rating": forms.NumberInput(attrs={"max": 10, "min": 0.0, "step": 0.1}),
        }
        
    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating is not None and (rating < 0 or rating > 10):
            raise forms.ValidationError("Рейтинг має бути від 0 до 10.")
        return rating

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and "pirated" in title.lower():
            raise forms.ValidationError("Заборонене слово 'pirated' у назві!")
        return title

    
