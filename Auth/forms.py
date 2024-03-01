from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserCreationForm(UserCreationForm):
    surname = forms.CharField(label='surname', max_length=50)
    name = forms.CharField(label='name', max_length=50)
    middlename = forms.CharField(label='surname', max_length=50)
    email = forms.EmailField(label='email', max_length=50)
    sex = forms.CharField(label='sex', max_length=1)
    phone_number = forms.CharField(label='phone_number', max_length=11)
    password = forms.PasswordInput(label='password', min_length=8, max_length=32)


