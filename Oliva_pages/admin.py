from django.contrib import admin
from .models import Review
from .models import Doctor
from .models import MedicalService
from .models import News

from .models import DoctorReview
from .models import Medical_Service_Review
from .models import NewsReview

admin.site.register(Review)
admin.site.register(Doctor)
admin.site.register(MedicalService)
admin.site.register(News)

#TODO: on prod there should not be reviews registered
admin.site.register(DoctorReview)
admin.site.register(Medical_Service_Review)
admin.site.register(NewsReview)