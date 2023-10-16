from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name=models.CharField(default="example", max_length=200)
    surname = models.CharField(default="example", max_length=200)  
    email = models.EmailField(default="example@example.com")
    message = models.CharField(blank=True, max_length=2000)
    avatar = models.CharField(blank=True, max_length=2000)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist=models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()
    
    def __str__(self):
        return self.text