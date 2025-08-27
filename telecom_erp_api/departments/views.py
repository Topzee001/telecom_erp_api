from django.shortcuts import render
from .serializers import DepartmentSerializer
from .permissions import IsAdminOrManager
from .models import Department
from rest_framework import generics, permissions

class DepartmentView(generics.ListCreateAPIView):
    queryset= Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrManager, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        serializer.save(created_by=self.request.user)

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Department.objects.all()
    serializer_class=DepartmentSerializer
    permission_classes=[permissions.IsAuthenticated, IsAdminOrManager]
