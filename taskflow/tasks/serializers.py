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
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "posted_by",
            "priority",
            "state",
            "home_tag",
            "work_tag",
            "university_tag",
            "social_tag",
            "completed",
            ]
        read_only_fields = ["id", "posted_by"]