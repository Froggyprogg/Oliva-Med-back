from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from Oliva_pages.models import Doctor, MedicalService, Review, WorkSchedule
from Oliva_pages.serializers import ReviewSerializer, WorkScheduleSerializer
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


class ReviewsListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


def list_doctors(request):
    doctors = Doctor.objects.all()
    args = {'questions': doctors}
    return render(request, "path_to/file.html", args)


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
#     return render(request, "path_to/file.html", args)
#

def list_medicalservice(request):
    service = MedicalService.objects.all()
    args = {'questions': service}
    return render(request, "path_to/file.html", args)


# def list_calendarevents(request):
#     events = CalendarEvents.objects.all()
#     args = {'questions': events}
#     return render(request, "path_to/file.html", args)
