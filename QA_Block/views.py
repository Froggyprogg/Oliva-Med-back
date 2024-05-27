from rest_framework import  generics
from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import Question
from .serializers import QuestionSerializer


class QuestionsListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer


class QuestionDetailView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'


class AnswerDetailView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'question'
