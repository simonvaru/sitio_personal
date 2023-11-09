from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def home(request):
    return HttpResponse("hello world!")

def index(response, id):
    ls=ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def cvsim(response):
    return render(response, "main/cvsim.html", {})

def demoapp1(response):
    return render(response, "main/demoapp1.html", {})

def demoapp2(response):
    return render(response, "main/demoapp2.html", {})

def demoapp3(response):
    response.user
    return render(response, "main/demoapp3.html", {})

def create(response):
    if response.method == "POST":
        form=CreateNewList(response.POST)
        
        if form.is_valid():
            todo=ToDoList(
            name=form.cleaned_data["name"],
            # surname=form.cleaned_data["surname"],
            email=form.cleaned_data["email"],
            message=form.cleaned_data["message"],
            # avatar=form.cleaned_data["avatar"],
            )
            todo.save()
        return HttpResponseRedirect("/%i" %todo.id)   
            
    else:    
        form=CreateNewList()
    return render(response, "main/create.html", {"form":form})


