from django.shortcuts import render
# from .models import ToDoList, Item
# from .forms import CreateNewList

# Create your views here.
def image_editor(response):
    return render(response, "app_im_ed.html", {})