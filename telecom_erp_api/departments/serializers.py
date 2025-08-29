from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    manager_name = serializers.CharField(source='manager.get_full_name', read_only=True)
    created_by_email = serializers.CharField(source='created_by.email', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    # total_users = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'manager', 'manager_name', 'created_by', 'created_by_name', 'created_by_email', 'created_at']
        read_only_fields = ['created_at', 'created_by']

        def get_total_users(self, obj):
            return obj.users.count()