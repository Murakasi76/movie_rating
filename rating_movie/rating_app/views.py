from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rating_app.forms import MovieForm

# Create your views here.

def index(request: HttpRequest):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = MovieForm()
    
    context = {
        "form": form
    }
    return render(request, 'rating_app/index.html', context)
