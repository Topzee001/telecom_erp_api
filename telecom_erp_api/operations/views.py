from .serializers import OperationSerializer, OperationsStatusUpdateSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Operations
from .permissions import canCreateOperation, CanReviewOperation


class OperationListCreateView(generics.ListCreateAPIView):
    serializer_class = OperationSerializer
    permission_classes = [permissions.IsAuthenticated, canCreateOperation]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return Operations.objects.all()
        # engineers can see operations they submitted
        return Operations.objects.filter(submitted_by=user)
    def perform_create(self, serializer):
        task = serializer.validated_data['task']

        # engineers create opr for their task
        if(self.request.user.role == 'ENGINEER' and task.assigned_to != self.request.user):
            raise PermissionDenied("You can only create a operation report for your own task assigned")
        
        serializer.save(submitted_by=self.request.user)

class OperationDetailsView(generics.RetrieveAPIView):
    queryset = Operations.objects.all()
    serializer_class= OperationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OperationStatusUpdateView(generics.UpdateAPIView):
    queryset = Operations.objects.all()
    serializer_class =OperationsStatusUpdateSerializer
    permission_classes= [permissions.IsAuthenticated, CanReviewOperation]

    def perform_update(self, serializer):
        operations = self.get_object()
        new_status = serializer.validated_data.get('status')
        user = self.request.user

        if new_status == 'reviewd':
            serializer.save(reviewed_by=user)
        if new_status == 'approved':
            serializer.save(reviewed_by=user)
        if new_status == 'rejected':
            serializer.save(reviewed_by=user)
        else:
            serializer.save()
