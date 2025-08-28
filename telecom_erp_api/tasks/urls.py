from django.urls import path
from .views import TaskListCreateView, TaskDetailView, MyTaskListView, TaskStatusUpdateView

urlpatterns = [
    """task management""",
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('status/<int:pk>/', TaskStatusUpdateView.as_view(), name='task-status-update'),
    """for engineers view""",
    path('my-tasks/', MyTaskListView.as_view(), name='my-tasks')

]