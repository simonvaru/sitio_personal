from django import forms 

class CreateNewList(forms.Form):
    name=forms.CharField(label="Name", max_length=200)
    surname=forms.CharField(label="Surname", max_length=200)
    email=forms.EmailField(label="Email")
    message=forms.CharField(required=False, label="Message", max_length=2000)
    avatar=forms.CharField(required=False, label="Avatar", max_length=200)
    check = forms.BooleanField(label="Ready to register")