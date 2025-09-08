from django.db import models
from django.core.validators import MinValueValidator
from users.models import User


class Priority(models.IntegerChoices):
    LOW = 1, "Baja"
    MEDIUM = 2, "Media"
    HIGH = 3, "Alta"


class State(models.IntegerChoices):
    TO_DO = 1, "Por Hacer"
    IN_PROGRESS = 2, "En Progreso"
    DONE = 3, "Hecho"


class Task(models.Model):
    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    state = models.IntegerField(choices=State.choices, default=State.TO_DO)
    home_tag = models.BooleanField(default=False)
    work_tag = models.BooleanField(default=False)
    university_tag = models.BooleanField(default=False)
    social_tag = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.posted_by.email}"
