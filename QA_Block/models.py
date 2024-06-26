from django.db import models
from django.conf import settings
from django.utils.text import slugify

from Oliva_pages.models import Doctor


class UserQAProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=True, primary_key=True)

    def __str__(self):
        return self.user.first_name


class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(help_text="Введите Вопрос",
                                   verbose_name="Вопрос",
                                   default="Вопрос")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    closed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField(help_text="Введите Ответ",
                                   verbose_name="Ответ",
                                   default="Ответ")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        return self.answer_text
