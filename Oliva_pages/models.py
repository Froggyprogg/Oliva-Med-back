from django.db import models
from OlivaMed import settings


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
    # education_photo
    # files
    # video
    # key to priem
    medical_service = models.ForeignKey(MedicalService, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs) #TODO: Надо чтобы шорткат создавался с моделью


class DoctorShortcut(models.Model): #TODO: ПОМЕНЯТЬ
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class DoctorReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    photo = models.FileField(verbose_name="Фото", upload_to="media/photo/news")
    text = models.TextField(verbose_name="Текст новости")
    likes = models.IntegerField(verbose_name="Лайки", default=0)

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)


class NewsShortcut(models.Model): #TODO: ПОМЕНЯТЬ
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class NewsReview(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, blank=True)
    review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)


class CalendarEvents(models.Model):
    date = models.DateTimeField(verbose_name='Дата события')
    description = models.CharField(verbose_name='Описание события')