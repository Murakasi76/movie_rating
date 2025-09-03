from django.urls import path
from rating_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
