from rest_framework import serializers
from .models import Operation
from uploads.serializers import UploadSerializer

class OperationSerializer(serializers.ModelSerializer):
    # fields to show names instead of IDs
    task_title = serializers.CharField(source='task.title', read_only=True)
    submitted_by_name = serializers.CharField(source='submitted_by.get_full_name', read_only=True)
    reviewed_by_name = serializers.CharField(source='reviewed_by.get_full_name', read_only=True)
    approved_by_name = serializers.CharField(source="approved_by.get_full_name", read_only=True)
    rejected_by_name = serializers.CharField(source="rejected_by.get_full_name", read_only=True)

    uploads = UploadSerializer(many=True, read_only=True)

    class Meta:
        model = Operation
        fields = [
            'id', 'task', 'task_title', 'operation_type', 'location', 'latitude', 
            'longitude', 'required_equipments', 'notes', 'status', 'submitted_by_name',
            'reviewed_by_name', 'approved_by_name', 'rejected_by_name', 'completed_at',
            'created_at', 'updated_at', 'uploads', 'approval_comments'
        ]
        # [
        #     'id', 'task', 'task_title', 'operation_type', 'notes', 'status',
        #     'submitted_by', 'submitted_by_name', 'reviewed_by', 'reviewed_by_name',
        #     'approved_by', 'approved_by_name', 'rejected_by', 'rejected_by_name', 'completed_at',
        #     'created_at', 'updated_at', 'uploads'
        # ]
        read_only = [
            'id', 'submitted_by_name', 'reviewed_by_name', 'approved_by_name',
            'rejected_by_name', 'completed_at', 'created_at', 'updated_at', 'status'
        ]
        # [
        #     'submitted_by', 'approved_by', 'rejected_by',
        #     'reviewed_by', 'completed_at', 'created_at', 'updated_at'
        # ]

class OperationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields=[
            'task', 'operation_type', 'latitude', 'longitude', 'location',
            'required_equipments', 'notes'
        ]

    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except Exception as e:
            print(f"Serialization error: {e}")
            print(f"Data causing error: {data}")
            raise

class OperationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['status', 'approval_comments']


