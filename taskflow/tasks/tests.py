from django.test import TestCase
from tasks.models import Task
from users.models import User


class TaskTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="John",
            last_name="Doe",
            email="john123@example.com",
            department=1,
            is_boss=False,
        )

        Task.objects.create(
            title="Task 1",
            description="Description for Task 1",
            created_at="2025-09-08T15:20:00",
            due_date="2025-09-10T15:20:00",
            completed=False,
            posted_by_id=1
        )
        
        Task.objects.create(
            title="Task 2",
            description="Description for Task 2",
            created_at="2025-09-08T15:20:00",
            due_date="2025-09-11T15:20:00",
            completed=False,
            posted_by_id=1
            )

    def test_task_creation(self):
        task1 = Task.objects.get(title="Task 1")
        task2 = Task.objects.get(title="Task 2")
        task2.completed = True
        task2.save()
        self.assertEqual(task1.completed, False)
        self.assertEqual(task2.completed, True)
