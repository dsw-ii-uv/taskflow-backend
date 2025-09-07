from rest_framework import generics, pagination
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        queryset = Task.objects.all().order_by("-created_at")
        user = self.request.query_params.get("posted_by")
        if user:
            queryset = Task.objects.filter(posted_by__id=user).order_by("-created_at")
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
