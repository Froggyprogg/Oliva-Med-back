from rest_framework import serializers

from Oliva_pages.models import Review, WorkSchedule, Doctor, Doctor_eduaction_photo, Doctor_files, Doctor_videos, \
    MedicalService, DoctorReview, Job


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'title', 'review_text', 'pub_date']
        read_only_fields = ['id', 'pub_date']

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)


class WorkScheduleSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = WorkSchedule
        fields = ['id', 'doctor', 'doctor_name', 'date', 'start_time', 'end_time', 'is_available']
        read_only_fields = ['doctor_name']

    def get_doctor_name(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"


class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = ['name', 'price']


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

    class Meta:
        model = Doctor
        fields = ['last_name', 'first_name', 'middlename', 'phone_number', 'sex', 'main_photo', 'medical_service', 'education_photos', 'files', 'video']


class DoctorReviewSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = DoctorReview
        fields = ['id', 'review', 'doctor']

    def create(self, validated_data):
        review = self.context['request'].data.get('review')
        doctor = self.context['request'].data.get('doctor')

        review_instance = Review.objects.create(
            user=self.context['request'].user,
            title=review['title'],
            review_text=review['review_text']
        )

        doctor_instance = Doctor.objects.get(id=doctor)

        return DoctorReview.objects.create(
            review=review_instance,
            doctor=doctor_instance
        )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'description', 'salary']