from rest_framework import serializers
from .models import Operations
from uploads.serializers import UploadSerializer

class OperationSerializer(serializers.ModelSerializer):
    # fields to show names instead of IDs
    task_title = serializers.CharField(source='tasks.title', read_only=True)
    submitted_by_name = serializers.CharField(source='submitted_by.get_full_name', read_only=True)
    reviewed_by_name = serializers.CharField(source='reviewed_by.get_full_name', read_only=True)
    approved_by_name = serializers.CharField(source="approved_by.get_full_name", read_only=True)
    rejected_by_name = serializers.CharField(source="rejected_by.get_full_name", read_only=True)

    uploads = UploadSerializer(many=True, read_only=True)

    class Meta:
        model = Operations
        fields = [
            'id', 'task', 'task_title', 'operation_type', 'notes', 'status',
            'submitted_by', 'submitted_by_name', 'reviewed_by', 'reviewed_by_name',
            'approved_by', 'approvec_by_name', 'rejected_by', 'rejected_by_name', 'completed_at',
            'created_at', 'updated_at', 'uploads'
        ]
        read_only = [
            'submitted_by', 'approved_by', 'rejected_by',
            'reviewed_by', 'completed_at', 'created_at', 'updated_at'
        ]

# class for manager to add comment when reviewing, incase of rejection
class OperationsStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ['status', 'notes']


