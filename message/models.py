from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField 
from django.core.validators import RegexValidator

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),]
    )
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


