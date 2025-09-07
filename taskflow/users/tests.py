from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john123@example.com",
            department=1,
            is_boss=False
            )
        User.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane123@example.com",
            department=2,
            is_boss=True
            )
    
    def test_user_creation(self):
        john = User.objects.get(first_name="John")
        jane = User.objects.get(first_name="Jane")
        self.assertEqual(john.first_name, "John")
        self.assertEqual(jane.last_name, "Doe")