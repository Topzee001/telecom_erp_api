# approvals/views.py
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Approval
from .serializers import ApprovalSerializer

class ApprovalCreateView(generics.CreateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        operation = serializer.validated_data['operation']
        
        # Check if manager is from the same department
        if (self.request.user.role == 'MANAGER' and 
            operation.task.department.manager != self.request.user):
            raise PermissionDenied("You can only review operations from your department")
        
        # Check if already reviewed
        if Approval.objects.filter(operation=operation, reviewed_by=self.request.user).exists():
            raise PermissionDenied("You have already reviewed this operation")
        
        serializer.save(reviewed_by=self.request.user)

class OperationApprovalsListView(generics.ListAPIView):
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        operation_id = self.kwargs['operation_id']
        return Approval.objects.filter(operation_id=operation_id)
    

    # add the below in the operations view if this seperate approval will be used
    """
    
    # operations/views.py
class OperationStatusUpdateView(generics.UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, CanReviewOperation]

    def perform_update(self, serializer):
        operation = self.get_object()
        new_status = serializer.validated_data.get('status')
        user = self.request.user

        # Track who performed each action
        if new_status == 'reviewed':
            serializer.save(reviewed_by=user)
        elif new_status == 'approved':
            serializer.save(approved_by=user, completed_at=timezone.now())
        elif new_status == 'rejected':
            serializer.save(rejected_by=user)
        else:
            serializer.save()
    
    """