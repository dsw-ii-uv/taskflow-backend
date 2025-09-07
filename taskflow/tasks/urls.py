from django.urls import path
from .views import TaskListCreateView, TaskDetail

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
]