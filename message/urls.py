from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('create/', views.contact, name='create'),
    path('success/', views.contact_success, name='success'),
]
