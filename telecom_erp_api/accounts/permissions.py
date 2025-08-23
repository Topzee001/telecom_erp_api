from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "ADMIN")
    
"""this allows user to access their details and admin can also access"""
class isSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return obj == user or getattr(user, 'role', None) == "ADMIN" # this checks if object being accessed by requesting user themselves or user.role == admin, and it returns non if role doesn't exist instead of crashing
    
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS