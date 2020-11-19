from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("adriel", views.adriel, name="adriel"),
    path("mary", views.mary, name="mary")
]