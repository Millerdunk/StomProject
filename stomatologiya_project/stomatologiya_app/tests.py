from django.test import TestCase
from django.urls import reverse
from .models import Patient, Service

class YourTestCase(TestCase):
    def setUp(self):
        # Подготовка данных для тестов
        self.patient = Patient.objects.create(
            first_name='John',
            email='john@example.com',
            message='Test message',
            phone_number='1234567890'
        )
        self.service = Service.objects.create(name='Test Service')

    def test_patient_creation(self):
        # Тест создания пациента
        self.assertEqual(self.patient.first_name, 'John')
        self.assertEqual(self.patient.email, 'john@example.com')

    def test_service_creation(self):
        # Тест создания услуги
        self.assertEqual(self.service.name, 'Test Service')

    def test_views(self):
        # Тестирование представлений
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        # Другие тесты представлений

   
