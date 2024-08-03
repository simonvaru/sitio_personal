from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'phone': forms.TextInput(attrs={'placeholder': '+999999999, 15 digits top'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@example.com'}),
        }