# Generated by Django 5.0.2 on 2024-03-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_Block', '0002_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(default='Ответ', help_text='Введите Ответ', verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(default='Вопрос', help_text='Введите Вопрос', verbose_name='Вопрос'),
        ),
    ]
