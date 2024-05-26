from datetime import datetime, timedelta

import jwt as jwt
from django.contrib.auth.models import AbstractUser, User
from django.db import models, transaction

from OlivaMed import settings

from django.contrib.auth.models import (
    BaseUserManager
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    surname = models.CharField(help_text="Введите фамилию",
                               verbose_name="Фамилия",
                               max_length=50)
    name = models.CharField(help_text="Введите имя",
                            verbose_name="Имя",
                            max_length=50)
    middlename = models.CharField(help_text="Введите Отчество(если есть)",
                                  verbose_name="Отчество",
                                  max_length=50)
    email = models.EmailField(help_text="Введите электронную почту",
                              verbose_name="Электронная почта",
                              max_length=50,
                              unique=True)
    sex = models.CharField(max_length=1,
                           help_text="Введите Пол",
                           verbose_name="Пол")
    phone_number = models.CharField(max_length=11,
                                    help_text="Введите номер телефона",
                                    verbose_name="Номер телефона",
                                    unique=True)
