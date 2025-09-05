from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rating_app.forms import MovieForm

# Create your views here.

def index(request: HttpRequest):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return HttpResponse("Date was saved")
    elif request.method == "GET":
        form = MovieForm()
    
    context = {
        "form": form
    }
    return render(request, 'rating_app/index.html', context)
