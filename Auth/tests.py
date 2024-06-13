import json

from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

from Auth.serializers import UserSerializer, LoginSerializer, PasswordResetSerializer


class UserCreateViewTest(TestCase):
    def test_create_user(self):
        data = {
            "username": "test_user",
            "email": "test@example.com",
            "password": "password123"
        }
        response = self.client.post(reverse('user-create'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(username='test_user')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123'))

class LoginViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')

    def test_login_success(self):
        data = {
            "username": "test_user",
            "password": "password123"
        }
        response = self.client.post(reverse('login'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)

    def test_login_fail(self):
        data = {
            "username": "test_user",
            "password": "wrong_password"
        }
        response = self.client.post(reverse('login'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.data)

class PasswordChangeViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')

    def test_password_change_success(self):
        self.client.force_login(self.user)
        data = {
            "old_password": "password123",
            "new_password": "new_password123"
        }
        response = self.client.put(reverse('password-change'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)

    def test_password_change_fail(self):
        self.client.force_login(self.user)
        data = {
            "old_password": "wrong_password",
            "new_password": "new_password123"
        }
        response = self.client.put(reverse('password-change'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.data)


class PasswordResetViewTest(TestCase):

    def test_password_reset_success(self):
        user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')
        data = {
            "email": "test@example.com"
        }
        response = self.client.post(reverse('password-reset'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)


class SerializerTests(TestCase):

    def test_user_serializer(self):
        user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')
        serializer = UserSerializer(user)
        expected_data = {
            'id': user.id,
            'username': 'test_user',
            'email': 'test@example.com'
        }
        self.assertEqual(serializer.data, expected_data)

    def test_login_serializer(self):
        serializer = LoginSerializer(data={
            "username": "test_user",
            "password": "password123"
        })
        self.assertTrue(serializer.is_valid())

    # def test_password_reset_serializer(self):
    #     serializer = PasswordResetSerializer(data={
    #         "email": "test@example.com"
    #     })
    #     self.assertTrue(serializer.is_valid())