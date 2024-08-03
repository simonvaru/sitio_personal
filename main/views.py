from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import CreateNewList



def index(response, id):
    ls=ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def cvsim(response):
    # x: bool = True
    # context = {'X': x}
    # return render(response, "main/cvsim.html", context)
# def cvsim(response):
#     x = True
#     return render(response, "main/cvsim.html", x)
    return render(response, "main/cvsim.html", {})

def demoapp1(response):
    return render(response, "main/demoapp1.html", {})

def demoapp2(response):
    return render(response, "main/demoapp2.html", {})

def demoapp3(response):
    response.user
    return render(response, "main/demoapp3.html", {})

# def create(request):
#     if request.method == "POST":
#         form=CreateNewList(request.POST)
        
#         if form.is_valid():
#             todo=ToDoList(
#             name=form.cleaned_data["name"],
#             email=form.cleaned_data["email"],
#             message=form.cleaned_data["message"],
#             )
#             todo.save()  
#         return redirect('success')
            
#     else:    
#         form=CreateNewList()
#     # return render(response, "main/create.html", {"form":form})        
#     return render(request, "main/create.html", {"form":form})

# def success(response):
#     return render(response, "main/success.html", {})


