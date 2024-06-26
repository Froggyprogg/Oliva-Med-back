# Generated by Django 5.0.2 on 2024-06-07 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oliva_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='doctor',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Oliva_pages.doctor'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('phone_number', models.CharField(help_text='Введите номер телефона', max_length=11, unique=True, verbose_name='Номер телефона')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_schedule', to='Oliva_pages.doctor')),
            ],
            options={
                'unique_together': {('doctor', 'date', 'phone_number')},
            },
        ),
    ]
