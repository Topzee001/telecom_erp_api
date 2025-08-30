from rest_framework.permissions import BasePermission

class canCreateOperation(BasePermission):
    """# ENGINEERS can create operations for their assigned tasks"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'MANAGER', 'ENGINEER']

class CanReviewOperation(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'MANAGER']
    
    # manager can only review operations from their department
    def has_object_permission(self, request, view, obj):
        return obj.task.department.manager == request.user or request.user.role == 'ADMIN'
