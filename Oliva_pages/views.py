from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from Oliva_pages.models import Doctor, News, MedicalService, CalendarEvents, Review
from Oliva_pages.serializers import ReviewSerializer


class ReviewCreateView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

def list_doctors(request):
    doctors = Doctor.objects.all()
    args = {'questions': doctors}
    return render(request, "path_to/file.html", args)


def list_news(request):
    news = News.objects.all()
    args = {'questions': news}
    return render(request, "path_to/file.html", args)


def list_medicalservice(request):
    service = MedicalService.objects.all()
    args = {'questions': service}
    return render(request, "path_to/file.html", args)


def list_calendarevents(request):
    events = CalendarEvents.objects.all()
    args = {'questions': events}
    return render(request, "path_to/file.html", args)