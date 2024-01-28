from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path("image_ed/", views.image_editor),
]