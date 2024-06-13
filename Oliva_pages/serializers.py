from rest_framework import serializers

from Oliva_pages.models import Doctor, Doctor_eduaction_photo, Doctor_files, Doctor_videos, \
    MedicalService, Review, Job, JobAppointment, Callback, WorkSchedule


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'title', 'review_text', 'pub_date', 'doctor']
        read_only_fields = ['id', 'pub_date', 'user']

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


class WorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields = ['id', 'doctor', 'phone_number', 'date']

    def get_doctor_name(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"


class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = ['name', 'price']


class DoctorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'title', 'review_text', 'pub_date', 'doctor']


class Doctor_eduaction_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_eduaction_photo
        fields = ['photo']


class Doctor_filesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_files
        fields = ['files']


class Doctor_videosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_videos
        fields = ['video']


class DoctorSerializer(serializers.ModelSerializer):
    education_photos = Doctor_eduaction_photoSerializer(many=True, read_only=True)
    files = Doctor_filesSerializer(many=True, read_only=True)
    video = Doctor_videosSerializer(many=True, read_only=True)
    reviews = DoctorReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['last_name', 'first_name', 'middlename', 'phone_number', 'sex', 'main_photo', 'spec', 'education_photos', 'files', 'video', 'reviews']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'description', 'salary']


class JobAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAppointment
        fields = ['job', 'fi', 'email', 'phone_number']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=JobAppointment.objects.all(),
                fields=['email'],
                message="Email already exists."
            )
        ]

    def create(self, validated_data):
        return JobAppointment.objects.create(**validated_data)


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = ['fi', 'email', 'phone_number', 'comment']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Callback.objects.all(),
                fields=['email'],
                message="Email already exists."
            )
        ]

    def create(self, validated_data):
        return Callback.objects.create(**validated_data)