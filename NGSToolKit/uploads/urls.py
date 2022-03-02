from .views import csv_file, home, visualize
from django.urls import path

urlpatterns = [
    path('home', home),
    path('', home),
    path('upload', csv_file ),
    path('visualize', visualize)
]

