from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=255),
    last_name=forms.CharField(max_length=255),
    email=forms.EmailField(),
    

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
