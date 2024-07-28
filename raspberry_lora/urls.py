from django.urls import path
from . import views

urlpatterns = [
path("raspberry_lora/", views.raspberry_lora),
]