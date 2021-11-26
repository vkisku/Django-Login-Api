from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.


class User(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        unique = ('email')
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
