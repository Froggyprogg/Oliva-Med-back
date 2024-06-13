from django.db import models
from OlivaMed import settings
from django.core.validators import FileExtensionValidator, MinLengthValidator


class MedicalService(models.Model):
    name = models.CharField(verbose_name="Название")
    description = models.CharField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")

    def save(self, *args, **kwargs):
        super(MedicalService, self).save(*args, **kwargs)


class Doctor(models.Model):
    last_name = models.CharField(verbose_name="Фамилия",
                                 max_length=50)
    first_name = models.CharField(verbose_name="Имя",
                                  max_length=50)
    middlename = models.CharField(verbose_name="Отчество",
                                  max_length=50)
    phone_number = models.CharField(max_length=11,
                                    verbose_name="Номер телефона",
                                    unique=True)
    sex = models.CharField(max_length=1,
                           verbose_name="Пол")
    main_photo = models.FileField(verbose_name="Главное фото", upload_to="media/photo/doctor")
    spec = models.CharField(verbose_name="Специальность",
                                 max_length=50)
    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs)


class Doctor_eduaction_photo(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='education_photos')
    photo = models.FileField(verbose_name="Фото образования", upload_to="media/photo/doctor/education")


class Doctor_files(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='files')
    files = models.FileField(verbose_name="Файлы статьей и т.д", upload_to="media/photo/doctor/files")


class Doctor_videos(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='video')
    video = models.FileField(verbose_name="Видео", upload_to="media/photo/doctor/videos",
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(help_text="Введите заголовок",
                             verbose_name="Заголовок")
    review_text = models.TextField(help_text="Введите свой отзыв",
                                   verbose_name="Отзыв")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)


class WorkSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='work_schedule')
    date = models.DateField(verbose_name='Дата')
    phone_number = models.CharField(max_length=11,
                                    help_text="Введите номер телефона",
                                    verbose_name="Номер телефона",
                                    unique=True)

    class Meta:
        unique_together = ('doctor', 'date', 'phone_number')

    def __str__(self):
        return f"{self.doctor.first_name} {self.doctor.last_name} - {self.date} "

    def save(self, *args, **kwargs):
        super(WorkSchedule, self).save(*args, **kwargs)


class Job(models.Model):
    name = models.CharField(verbose_name='Название вакансии')
    description = models.CharField(verbose_name='Описание')
    salary = models.IntegerField(verbose_name='Зарплата')


class JobAppointment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    fi = models.CharField(verbose_name='Фамилия Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=11,
                                    help_text="Введите номер телефона",
                                    verbose_name="Номер телефона",
                                    unique=True)


class Callback(models.Model):
    fi = models.CharField(verbose_name='Фамилия Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=11,
                                    help_text="Введите номер телефона",
                                    verbose_name="Номер телефона",
                                    unique=True)
    comment = models.CharField(verbose_name='Комментарий')
