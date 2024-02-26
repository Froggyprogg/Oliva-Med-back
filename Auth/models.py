from datetime import datetime, timedelta

import jwt as jwt
from django.contrib.auth.models import AbstractUser
from django.db import models

from OlivaMed import settings


class User(AbstractUser):
    surname = models.CharField(help_text="Введите фамилию",
                                    verbose_name="Фамилия")
    name = models.CharField(help_text="Введите имя",
                               verbose_name="Имя")
    middlename = models.CharField(help_text="Введите Отчество(если есть)",
                               verbose_name="Отчество")
    phone_number = models.CharField(max_length=11,
                                    help_text="Введите номер телефона",
                                    verbose_name="Номер телефона",
                                    unique=True)
    email = models.EmailField(help_text="Введите электронную почту",
                              verbose_name="Электронная почта",
                              unique=True,)
    sex = models.CharField(max_length=1,
                           help_text="Введите Пол",
                           verbose_name="Пол")
    password = models.CharField(max_length=128,
                                help_text="Введите пароль",
                                verbose_name="Пароль")

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