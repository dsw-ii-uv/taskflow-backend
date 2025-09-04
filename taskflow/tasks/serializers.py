from django.utils import timezone
from rest_framework import serializers
from tasks.models import Task
from users.models import User


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]
        read_only_fields = fields


class TaskSerializer(serializers.ModelSerializer):
    posted_by = TaskUserSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ["is_active"]
        read_only_fields = ["created_at"]