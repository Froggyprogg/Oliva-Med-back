from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from Oliva_pages.models import Doctor, MedicalService, Review, Job, JobAppointment, WorkSchedule
from Oliva_pages.serializers import ReviewSerializer, DoctorSerializer, \
    MedicalServiceSerializer, JobSerializer, JobAppointmentSerializer, CallbackSerializer, WorkScheduleSerializer
from django.views.decorators.csrf import csrf_exempt


class ReviewCreateView(APIView):

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDoctorReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentCreateView(CreateAPIView):
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer

    def perform_create(self, serializer):
        work_schedule = serializer.save()
        work_schedule.is_available = False
        work_schedule.save()


class MedicalServiceListView(ListAPIView):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer

    def list(self, request, *args, **kwargs):
        response = super(MedicalServiceListView, self).list(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response


class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class CallbackView(generics.CreateAPIView):
    serializer_class = CallbackSerializer

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class JobAppointmentView(generics.CreateAPIView):
    serializer_class = JobAppointmentSerializer

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)