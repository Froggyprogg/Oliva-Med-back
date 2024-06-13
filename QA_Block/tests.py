from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.test import APIRequestFactory

User = get_user_model()


class QuestionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='a576833r')

    def test_question_creation(self):
        question = Question.objects.create(
            title='Test Question',
            description='This is a test question.',
            user=self.user
        )
        self.assertEqual(question.title, 'Test Question')
        self.assertEqual(question.description, 'This is a test question.')
        self.assertEqual(question.user, self.user)
        self.assertFalse(question.closed)
        self.assertIsNotNone(question.slug)

    def test_question_all_serializer(self):
        question = Question.objects.create(
            title='Test Question',
            description='This is a test question.',
            user=self.user
        )
        factory = APIRequestFactory()
        request = factory.get('api/questions/')


    def test_question_with_pk_serializer(self):
        question = Question.objects.create(
            title='Test Question',
            description='This is a test question.',
            user=self.user
        )
        factory = APIRequestFactory()
        request = factory.get('api/questions/1')