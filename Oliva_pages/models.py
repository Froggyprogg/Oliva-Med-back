from django.db import models
from OlivaMed import settings
from django.core.validators import FileExtensionValidator


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(help_text="Введите заголовок",
                             verbose_name="Заголовок")
    review_text = models.TextField(help_text="Введите свой отзыв",
                                   verbose_name="Отзыв")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)


class MedicalService(models.Model):
    name = models.CharField(verbose_name="Название")

    def save(self, *args, **kwargs):
        super(MedicalService, self).save(*args, **kwargs)


class Medical_Service_Review(models.Model):
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)
    medical_service = models.ForeignKey(MedicalService, on_delete=models.SET_NULL, null=True, blank=True)


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
    medical_service = models.ForeignKey(MedicalService, on_delete=models.SET_NULL, null=True, blank=True)

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


class WorkSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='work_schedule')
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(verbose_name='Время начала')
    end_time = models.TimeField(verbose_name='Время окончания')
    is_available = models.BooleanField(default=True, verbose_name='Доступен для записи')

    class Meta:
        unique_together = ('doctor', 'date', 'start_time', 'end_time')

    def __str__(self):
        return f"{self.doctor.first_name} {self.doctor.last_name} - {self.date} ({self.start_time} - {self.end_time})"

    def save(self, *args, **kwargs):
        super(WorkSchedule, self).save(*args, **kwargs)


class DoctorReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)


# class News(models.Model):
#     title = models.CharField(verbose_name="Заголовок")
#     pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
#     photo = models.FileField(verbose_name="Фото", upload_to="media/photo/news")
#     text = models.TextField(verbose_name="Текст новости")
#     likes = models.IntegerField(verbose_name="Лайки", default=0)
#
#     def save(self, *args, **kwargs):
#         super(News, self).save(*args, **kwargs)

# class NewsReview(models.Model):
#     news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, blank=True)
#     review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)


# class CalendarEvents(models.Model):
#     date = models.DateTimeField(verbose_name='Дата события')
#     description = models.CharField(verbose_name='Описание события')
