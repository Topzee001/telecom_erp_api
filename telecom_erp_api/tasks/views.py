from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsManagerOrAdmin, CanViewOrUpdateTask

class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsManagerOrAdmin, permissions.IsAuthenticated]

    def get_queryset(self):
        # show only assigned tasks to others, show all other tasks to manager/admin
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

class TaskDetailView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CanViewOrUpdateTask, permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Engineers can only update status to a specific value.
        allowed_statuses = ['in_progress', 'completed']
        new_status=serializer.validated_data.get('status')

        if new_status not in allowed_statuses:
            raise serializer.ValidationError({"status": "Invalid status update"})
        
        serializer.save()

