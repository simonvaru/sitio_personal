from django.urls import path

from . import views

urlpatterns = [
    path('p2/', views.demoapp2, name='demoapp2'),
]
