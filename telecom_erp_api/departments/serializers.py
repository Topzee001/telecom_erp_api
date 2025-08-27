from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    manager_name = serializers.CharField(source='manager.get_full_name', read_only=True)
    total_users = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'description', 'manager', 'manager_name', 'total_users', 'created_at']
        read_only_fields = ['created_at']

        def get_total_users(self, obj):
            return obj.users.count()