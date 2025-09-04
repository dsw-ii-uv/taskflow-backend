from django.db import models
from django.core.validators import MinValueValidator
from users.models import User


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Task(models.Model):
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    objects = TaskManager()

    def __str__(self):
        return self.title
