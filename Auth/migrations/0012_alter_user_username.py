# Generated by Django 5.0.2 on 2024-03-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0011_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(help_text='Введите электронную почту', max_length=50, unique=True, verbose_name='Электронная почта'),
        ),
    ]