from importlib.resources import path
from unicodedata import name
from django.urls import path
from .views import hola

urlpatterns = [
    path("hola-mundo/", hola, name="hola"),
]