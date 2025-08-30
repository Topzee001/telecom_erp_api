# approvals/serializers.py
from rest_framework import serializers
from .models import Approval

class ApprovalSerializer(serializers.ModelSerializer):
    reviewed_by_name = serializers.CharField(source='reviewed_by.get_full_name', read_only=True)
    operation_title = serializers.CharField(source='operation.task.title', read_only=True)

    class Meta:
        model = Approval
        fields = ['id', 'operation', 'operation_title', 'reviewed_by', 'reviewed_by_name', 
                 'status', 'comments', 'reviewed_at']
        read_only_fields = ['reviewed_by', 'reviewed_at']

    def validate(self, attrs):
        # Managers can only approve/reject operations from their department
        operation = self.instance.operation if self.instance else attrs.get('operation')
        if operation and operation.task.department.manager != self.context['request'].user:
            raise serializers.ValidationError("You can only review operations from your department")
        return attrs