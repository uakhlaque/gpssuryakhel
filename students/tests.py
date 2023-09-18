import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            student_number=random.randint(10000, 99999),
            first_name='Bob',
            last_name='Smith',
            father_name='ben',
            b_form_no='12345-1234567-9',
            dob='',
            age='',
            class_name='',
            contact='',
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
