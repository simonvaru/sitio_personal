from django.urls import path

from . import views

urlpatterns = [
    path('cv/', views.cvsim, name='cvsim'),
]
