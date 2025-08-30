from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer, TaskStatusUpdateSerializer
from .permissions import IsManagerOrAdmin, CanViewOrUpdateTask, CanViewTasks
from django.db.models import Count, Q

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CanViewTasks, permissions.IsAuthenticated]

    # def get_queryset(self):
    #     # show only assigned tasks to others, show all other tasks to manager/admin
    #     user = self.request.user
    #     if user.role in ['ADMIN', 'MANAGER']:
    #         return Task.objects.all()
    #     return Task.objects.filter(assigned_to=user)
    
    def perform_create(self, serializer):
        if self.request.user.role not in ['ADMIN', 'MANAGER']:
            raise PermissionDenied("only admins and manager can create tasks")
        serializer.save(created_by=self.request.user)
        # return super().perform_create(serializer)

class TaskDetailView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsManagerOrAdmin,
        # CanViewOrUpdateTask, 
        permissions.IsAuthenticated]
    
    # since i created tast status update class seperately, this is no longer needed
    # def get_serializer_class(self):
    #     if self.request.user in ['ADMIN', 'MANAGER']:
    #         return TaskSerializer
    #     return TaskStatusUpdateSerializer
    
    # def get_serializer(self, *args, **kwargs):
    #     serializer_class = self.get_serializer_class()
    #     kwargs['context'] = self.get_serializer_context()
    #     return serializer_class(*args, **kwargs)
    
    # def perform_update(self, serializer):
    #     # skip status validation for admins & managers
    #     user = self.request.user
    #     if user.role in ['ADMIN', 'MANAGER']:
    #         serializer.save()
    #         return
    #     # Engineers can only update status to a specific value.
    #     allowed_statuses = ['in_progress', 'completed']
    #     new_status=serializer.validated_data.get('status')

    #     if new_status not in allowed_statuses:
    #         raise ValidationError({"status": "Invalid status update"})
        
    #     serializer.save()

class TaskStatusUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CanViewOrUpdateTask]

    def perform_update(self, serializer):
        allowed_status = ['in_progress', 'completed']
        new_status = serializer.validated_data.get('status')

        if new_status not in allowed_status:
            raise ValidationError({"status": "Invalid status update"})
        
        serializer.save()

class MyTaskListView(generics.ListAPIView):
    """Engineers can see only their assigned tasks"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
    

class TaskSummaryView(generics.ListAPIView):
    permission_classes= [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.role not in ['ADMIN', 'MANAGER']:
            return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)
        
        summary = Task.objects.aggregate(
            total_tasks=Count('id'),
            pending_tasks = Count('id', filter=Q(status='pending')),
            completed_tasks=Count('id', filter=Q(status='completed'))
        )
        return Response(summary)