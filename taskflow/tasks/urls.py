from django.urls import path
from .views import TaskListCreateView, TaskDetail

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="task-list-create"),
    path("<int:pk>/", TaskDetail.as_view(), name="task-detail"),
]