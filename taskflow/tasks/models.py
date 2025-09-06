from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

class Task(models.Model):
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.posted_by.email}"
