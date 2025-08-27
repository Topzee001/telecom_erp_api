from django.urls import path
from .views import TaskCreateView, TaskDetailView

urlpatterns = [
    path('', TaskCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail')

]