from django.contrib import admin
from .models import Review, Doctor_eduaction_photo, Doctor_files, Doctor_videos, Job, WorkSchedule
from .models import Doctor
from .models import MedicalService


admin.site.register(Review)
admin.site.register(Doctor)
admin.site.register(WorkSchedule)
admin.site.register(MedicalService)
admin.site.register(Doctor_eduaction_photo)
admin.site.register(Doctor_files)
admin.site.register(Doctor_videos)
admin.site.register(Job)

