from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionSerializer


def list_questions(request):
    questions = Question.objects.all()
    args = {'questions': questions}
    return render(request, "path_to/file.html", args)


class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)