from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):
    """can perform CRUD operations"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['MANAGER', 'ADMIN']
    
class CanViewOrUpdateTask(BasePermission):
    """can view and update task status"""
    def has_object_permission(self, request, view, obj):
        # admin/manager can always access
        if request.user.role in ['ADMIN', 'MANAGER']:
            return True
        
        # assigned user can view and update status
        if request.user == obj.assigned_to:
            return True
        return False
