from django.urls import path
from .views import (
    TaskListCreateView, TaskDetailView, 
    TaskStatusUpdateView, MyTaskListView, 
    TaskSummaryView)
# , MyTaskListView, TaskStatusUpdateView

urlpatterns = [

    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('details/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('status/<int:pk>/', TaskStatusUpdateView.as_view(), name='task-status-update'),

    path('my-tasks/', MyTaskListView.as_view(), name='my-tasks'),
    path('summary/', TaskSummaryView.as_view(), name='task-summary')

]