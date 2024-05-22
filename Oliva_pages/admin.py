from django.contrib import admin
from .models import Review, WorkSchedule, Doctor_eduaction_photo, Doctor_files, Doctor_videos
from .models import Doctor
from .models import MedicalService
from .models import DoctorReview
from .models import Medical_Service_Review


admin.site.register(Review)
admin.site.register(Doctor)
admin.site.register(WorkSchedule)
admin.site.register(MedicalService)
admin.site.register(Doctor_eduaction_photo)
admin.site.register(Doctor_files)
admin.site.register(Doctor_videos)

admin.site.register(DoctorReview)
admin.site.register(Medical_Service_Review)
