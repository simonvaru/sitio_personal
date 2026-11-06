from django.urls import path

from . import views

urlpatterns = [
    path('p3/', views.demoapp3, name='demoapp3'),
]
