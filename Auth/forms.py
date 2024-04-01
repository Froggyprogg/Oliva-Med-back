from django.contrib.auth.forms import UserCreationForm
from django import forms
from rest_framework.exceptions import ValidationError

from .models import User


class UserCreationForm(UserCreationForm):
    surname = forms.CharField(label='surname', max_length=50)
    name = forms.CharField(label='name', max_length=50)
    middlename = forms.CharField(label='surname', max_length=50)
    email = forms.EmailField(label='email', max_length=50)
    sex = forms.CharField(label='sex', max_length=1)
    phone_number = forms.CharField(label='phone_number', max_length=11)
    password = forms.PasswordInput(label='password', min_length=8, max_length=32)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user




