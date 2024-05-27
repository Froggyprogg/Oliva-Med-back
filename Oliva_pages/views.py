from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from Oliva_pages.models import Doctor, MedicalService, Review, WorkSchedule, Job, DoctorReview
from Oliva_pages.serializers import ReviewSerializer, WorkScheduleSerializer, DoctorSerializer, \
    MedicalServiceSerializer, JobSerializer, DoctorReviewSerializer
from .serializers import WorkScheduleSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError


class ReviewCreateView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDoctorReviewView(generics.CreateAPIView):
    queryset = DoctorReview.objects.all()
    serializer_class = DoctorReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DoctorReviewListView(generics.ListAPIView):
    serializer_class = DoctorReviewSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return DoctorReview.objects.filter(doctor_id=doctor_id)


class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class WorkScheduleListView(ListAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer


class WorkScheduleListViewWithFilter(ListAPIView): # TODO: Возможно так лучше использовать
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['doctor', 'date', 'is_available']
    search_fields = ['doctor__first_name', 'doctor__last_name']
    ordering_fields = ['date', 'start_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        is_available = self.request.query_params.get('is_available', None)
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available)
        return queryset


class AppointmentCreateView(CreateAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer

    def perform_create(self, serializer):
        work_schedule = serializer.save()
        work_schedule.is_available = False
        work_schedule.save()


class AppointmentCreateViewWithFilter(CreateAPIView): # TODO: Возможно так лучше использовать
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer

    def perform_create(self, serializer):
        doctor = serializer.validated_data['doctor']
        date = serializer.validated_data['date']
        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']


        if WorkSchedule.objects.filter(doctor=doctor, date=date, start_time=start_time, end_time=end_time).exists():
            raise ValidationError("Это время уже занято.")

        work_schedule = serializer.save()
        work_schedule.is_available = False
        work_schedule.save()


# def list_news(request):
#     news = News.objects.all()
#     args = {'questions': news}


class MedicalServiceListView(ListAPIView):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer


# def list_calendarevents(request):
#     events = CalendarEvents.objects.all()
#     args = {'questions': events}

class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer