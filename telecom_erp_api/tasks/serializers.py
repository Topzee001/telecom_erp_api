from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.CharField(source='assigned_to.get_full_name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']

class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    """Engineers can have access to only update status"""
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status'] 
        read_only = ['id', 'title', 'description']
