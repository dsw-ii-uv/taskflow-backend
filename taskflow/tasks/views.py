from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if user.is_boss:
            return Task.objects.all()
        return Task.objects.filter(posted_by=user)
    
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.posted_by:
            raise PermissionDenied("You do not have permission to edit this task.")
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        if self.request.user != instance.posted_by:
            raise PermissionDenied("You do not have permission to delete this task.")
        instance.is_active = False
        instance.save()