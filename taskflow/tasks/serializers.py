from rest_framework import serializers
from tasks.models import Task
from users.models import User


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
        read_only_fields = fields


class TaskSerializer(serializers.ModelSerializer):
    posted_by = TaskUserSerializer( read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "completed", "posted_by"]
        read_only_fields = ["id", "posted_by"]