from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
path("<int:id>/", views.index, name="index"),   
#path("home/", views.home, name="home"),  
#path("index/", views.home, name="index"), 
path("home/", views.home, name="home"),
path("", views.home, name="home"),
#path("home", views.home, name="home"),
#path("index/", views.home, name="index"),
path("cv/", views.cvsim, name="cvsim"),
path("p1/", views.demoapp1, name="demoapp1"),
path("p2/", views.demoapp2, name="demoapp2"),
path("p3/", views.demoapp3, name="demoapp3"),
path("create/", views.create, name="create"),
path('success/', views.success, name='success'),
path('image_editor/', include('image_editor.urls')), 
# path('image_editor/', views.image_editor, name='image_editor'),
]
 