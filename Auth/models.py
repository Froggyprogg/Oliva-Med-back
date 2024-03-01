from datetime import datetime, timedelta

import jwt as jwt
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction

from OlivaMed import settings

from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractUser):
    # TODO:Решить проблему с необходимостью вводить Username при создании пользователя
    surname = models.CharField(help_text="Введите фамилию",
                               verbose_name="Фамилия",
                               max_length=50)
    name = models.CharField(help_text="Введите имя",
                            verbose_name="Имя",
                            max_length=50)
    middlename = models.CharField(help_text="Введите Отчество(если есть)",
                                  verbose_name="Отчество",
                                  max_length=50)
    phone_number = models.CharField(max_length=11,
                                    help_text="Введите номер телефона",
                                    verbose_name="Номер телефона",
                                    unique=True)
    email = models.EmailField(help_text="Введите электронную почту",
                              verbose_name="Электронная почта",
                              max_length=50,
                              unique=True, )
    sex = models.CharField(max_length=1,
                           help_text="Введите Пол",
                           verbose_name="Пол")
    # TODO: Нужно решить проблему с сохранением пароля, нужносохранять хэш
    password = models.CharField(max_length=128,
                                help_text="Введите пароль",
                                verbose_name="Пароль")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['surname', 'name', 'phone_number']
    objects = UserManager()

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 7 дней от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
