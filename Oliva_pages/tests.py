from django.test import TestCase
from .models import Doctor, Job
from .serializers import JobSerializer, JobAppointmentSerializer, CallbackSerializer


class DoctorTestCase(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            last_name="Иванов",
            first_name="Иван",
            middlename="Иванович",
            phone_number="89001234567",
            sex="М",
            main_photo="photo.jpg",
            spec="Test"
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.last_name, "Иванов")
        self.assertEqual(self.doctor.first_name, "Иван")
        self.assertEqual(self.doctor.middlename, "Иванович")
        self.assertEqual(self.doctor.phone_number, "89001234567")
        self.assertEqual(self.doctor.sex, "М")
        self.assertEqual(self.doctor.main_photo, "photo.jpg")
        self.assertEqual(self.doctor.spec, "Test")

    def test_doctor_save(self):
        self.doctor.last_name = "Петров"
        self.doctor.save()
        updated_doctor = Doctor.objects.get(pk=self.doctor.pk)
        self.assertEqual(updated_doctor.last_name, "Петров")


class TestJobSerializer(TestCase):

    def test_valid_data(self):
        data = {
            'name': 'Software Engineer',
            'description': 'Design and develop software applications.',
            'salary': 100000
        }
        serializer = JobSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        data = {
            'description': 'Design and develop software applications.',
            'salary': 100000
        }
        serializer = JobSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class TestJobAppointmentSerializer(TestCase):

    def test_valid_data(self):
        job = Job.objects.create(name='Software Engineer', description='Design and develop software applications.', salary=100000)
        data = {
            'job': job.id,
            'fi': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '88005553535'
        }
        serializer = JobAppointmentSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        data = {
            'fi': 'John Doe',
            'email': 'john.doe@example.com',
        }
        serializer = JobAppointmentSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_unique_email(self):
        job = Job.objects.create(name='Software Engineer', description='Design and develop software applications.', salary=100000)
        data = {
            'job': job.id,
            'fi': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '88005553535'
        }
        serializer1 = JobAppointmentSerializer(data=data)
        serializer1.is_valid()
        serializer1.save()

        data2 = {
            'job': job.id,
            'fi': 'Jane Doe',
            'email': 'john.doe@example.com',
            'phone_number': '88005553534'
        }
        serializer2 = JobAppointmentSerializer(data=data2)
        self.assertFalse(serializer2.is_valid())


class TestCallbackSerializer(TestCase):

    def test_valid_data(self):
        data = {
            'fi': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '88005553534',
            'comment': 'I am interested in the Software Engineer position.'
        }
        serializer = CallbackSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        data = {
            'fi': 'John Doe',
            'comment': 'I am interested in the Software Engineer position.'
        }
        serializer = CallbackSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_unique_email(self):
        data = {
            'fi': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '88005553534',
            'comment': 'I am interested in the Software Engineer position.'
        }
        serializer1 = CallbackSerializer(data=data)
        serializer1.is_valid()
        serializer1.save()

        data2 = {
            'fi': 'Jane Doe',
            'email': 'john.doe@example.com',
            'phone_number': '88005553536',
            'comment': 'I am interested in the Web Developer position.'
        }
        serializer2 = CallbackSerializer(data=data2)
        self.assertFalse(serializer2.is_valid())